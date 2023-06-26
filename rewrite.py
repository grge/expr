from expr import Expression, Symbol, Function
from match import match
from substitute import substitute
from typing import List, Tuple

def rewrite(expr: Expression, rules: List[Tuple[Expression, Expression]], max_rewrites: int = 10) -> Expression:
    if max_rewrites <= 0:
        return expr

    for pattern, replacement in rules:
        subs = match(expr, pattern)
        if subs is not None:
            expr = substitute(replacement, subs)
            max_rewrites -= 1
            break

    if isinstance(expr, Function):
        new_operands = [rewrite(operand, rules, max_rewrites) for operand in expr.operands]
        expr = type(expr)(*new_operands)

    return expr
