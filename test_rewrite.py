from rewrite import rewrite
from expr import Symbol

def test_rewrite_basic():
    x = Symbol('x')
    y = Symbol('y')
    rules = [(x, x*x)]
    assert rewrite(y + 2, rules, max_rewrites=1) == (y + 2)*(y + 2)

def test_rewrite_expand():
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    x = Symbol('x')
    y = Symbol('y')
    rules = [(a*(b + c), a*b + a*c)]
    assert rewrite(x*(y + 3), rules) == x*y + x*3

def test_rewrite_basic():
    x = Symbol('x')
    y = Symbol('y')
    rules = [(x + x, 2 * x)]
    expr = x + x
    rewritten_expr = rewrite(expr, rules)
    assert rewritten_expr == 2 * x

def test_rewrite_nested():
    x = Symbol('x')
    y = Symbol('y')
    rules = [(x + x, 2 * x)]
    expr = (x + x) * y
    rewritten_expr = rewrite(expr, rules)
    assert rewritten_expr == (2 * x) * y


def test_rewrite_no_match():
    x = Symbol('x')
    y = Symbol('y')
    rules = [(x * x, x + x)]
    expr = x * y
    rewritten_expr = rewrite(expr, rules)
    assert rewritten_expr == x * y
