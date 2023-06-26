from expr import Symbol, Literal
from substitute import substitute

def test_subs_symbol_for_literal():
    x = Symbol('x')
    subs = {x: 2}
    assert substitute(x, subs) == Literal(2)

def test_subs_symbol_for_symbol():
    x = Symbol('x')
    y = Symbol('y')
    subs = {x: y}
    assert substitute(x, subs) == y

def test_subs_symbol_for_self():
    x = Symbol('x')
    subs = {x: x}
    assert substitute(x, subs) == x

def test_subs_empty_subs():
    x = Symbol('x')
    subs = {}
    assert substitute(x, subs) == x

def test_subs_multiple_symbols():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    expr = 4*x*y
    subs = {x: z, y: 2}
    assert substitute(expr, subs) == 4*z*2



