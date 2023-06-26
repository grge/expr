
from substitute import substitute
from expr import Expression, Symbol, Function, Literal
from typing import List, Tuple, Dict, Optional

Subs = Dict[Symbol, Expression]

def match_many(exprs: List[Tuple[Expression, Expression]], subs: Subs) -> Subs:
    match exprs:
        case []:
            return subs

        case [(match, Symbol(name) as pattern), *rest]:
            if pattern in subs:
                if subs[pattern] == match:
                    return match_many(rest, subs)
                else:
                    return None
            else:
                return match_many(rest, {pattern:match} | subs)

        case [(Function() as match, Function() as pattern), *rest]:
            if type(match) == type(pattern) and match.arity == pattern.arity:
                return match_many([*zip(match.operands, pattern.operands), *rest], subs)
            else:
                return None
    
        case [(Literal() as match, Literal() as pattern), *rest] if match == pattern:
            return match_many(rest, subs)

        case _:
            return None


def match(expr: Expression, pattern: Expression) -> Optional[Subs]:
    """Return subs such that substitute(pattern, subs) == expr"""
    return match_many([(expr, pattern)], {})

