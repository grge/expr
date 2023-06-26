from dataclasses import dataclass
from numbers import Number

class Expression:
    def long_form(self, indent: int = 0) -> str:
        class_name = type(self).__name__
        match self:
            case Function():
                return (
                  class_name +
                  "(" + 
                  ",".join([op.long_form(indent + 1) for op in self.operands]) +
                  ")"
                )
            case _:
                return f"{class_name}({self})"

    def __eq__(self, other):
        return self.long_form() == other.long_form()


def ensure_expression(expr : Expression | Number):
    match expr:
        case Expression():
            return expr
        case Number():
            return Literal(expr)


def nested_repr(expression: 'Expression', outer_precedence: int = 0) -> str:
    precedence = getattr(type(expression), 'precedence', 0)
    result = str(expression)
    if precedence and precedence < outer_precedence:
        return f"({result})"
    return result


@dataclass(frozen=True)
class Symbol(Expression):
    name: str

    def __repr__(self):
        return self.name

@dataclass(frozen=True)
class Literal(Expression):
    value: Number

    def __repr__(self):
        return str(self.value)

class Function(Expression):
    precedence : int = 1
    infix_repr : bool = False
    repr_operator : str = None

    def __init__(self, *args, operands : list = None):
        if args is not None:
            self.operands = args
        else:
            self.operands = operands

    @property
    def arity(self):
        return len(self.operands)

    def __repr__(self):
        if self.infix_repr:
            return self.repr_operator.join(
                    [nested_repr(operand, self.precedence)
                     for operand in self.operands]
                   )
        else:
            op = (self.repr_operator
                   if self.repr_operator is not None
                   else self.__class__.__name__
                  )

            return f"{op}({','.join([nested_repr(operand, self.precedence) for operand in self.operands])})"


def create_binop_class(name, precedence, dunder_method, rdunder_method, repr_operator):
    BinOpCls = type(name,(Function,),
                    dict(precedence=precedence,
                         infix_repr=True,
                         repr_operator=repr_operator))

    def dunder_func(self, other):
        return BinOpCls(self, ensure_expression(other))

    def rdunder_func(self, other):
        return BinOpCls(ensure_expression(other), self)

    setattr(Expression, dunder_method, dunder_func)
    setattr(Expression, rdunder_method, rdunder_func)

    return BinOpCls


def create_unaryop_class(name, precedence, dunder_method, repr_operator):
    UnaryOpCls = type(name, (Function,),
                      dict(precedence=precedence,
                           infix_repr=False,
                           repr_operator=repr_operator))

    setattr(Expression, dunder_method, lambda self: UnaryOpCls(self))
    return UnaryOpCls


def create_constant(name, precedence=0, repr=None):
    ConstantCls = type(name, (Function, ),
                       dict(precedence=precedence,
                            infix_repr=False,
                            repr_operator=None))

    def repr_method(self):
        if repr is None:
            return self.__class__.__name__
        elif isinstance(repr, str):
            return repr
        else:
            return repr(self)

    ConstantCls.__repr__ = repr_method
    return ConstantCls()

        
Sum = create_binop_class("Sum", 2, "__add__", "__radd__", "+")
Sub = create_binop_class("Sub", 2, "__sub__", "__rsub__", "-")
Mul = create_binop_class("Mul", 3, "__mul__", "__rmul__", "*")
Pow = create_binop_class("Pow", 6, "__pow__", "__rpow__", "**")
Quotient = create_binop_class("Quotient", 5, "__truediv__", "__rtruediv__", "/")
Negate = create_unaryop_class("Negate", 2, "__neg__", "-")
Positive = create_unaryop_class("Positive", 2, "__pos__", "+")
