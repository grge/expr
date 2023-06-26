from expr import Expression, Symbol, Function, Literal, ensure_expression
from typing import Dict

def substitute(expr:Expression, subs:Dict[Symbol, Expression]) -> Expression:
    match expr:
        case Symbol(name):
            return ensure_expression(subs.get(expr, expr))
        case Literal():
            return expr
        case Function():
            return type(expr)(*[substitute(op, subs) for op in expr.operands])
