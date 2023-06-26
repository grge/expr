from expr import Symbol, Literal
from match import match

def test_match_symbol_for_symbol():
    x = Symbol('x')
    y = Symbol('y')
    assert match(y, x) == {x: y}

def test_match_symbol_for_function():
    x = Symbol('x')
    y = Symbol('y')
    assert match(y*y + y*y, x + x) == {x: y*y}

def test_match_two_symbols():
    x = Symbol('x')
    y = Symbol('y')
    a = Symbol('a')
    assert match(x*x*2, y*y*a) == {y: x, a: Literal(2)}

def test_match_no_match():
    x = Symbol('x')
    y = Symbol('y')
    assert match(x + 1, y - 1) is None

def test_match_function_for_function():
    x = Symbol('x')
    y = Symbol('y')
    assert match(3*x + 5, 3*y + 5) == {y: x}

def test_match_same_symbol_cant_match_twice():
    x = Symbol('x')
    y = Symbol('y')
    a = Symbol('a')
    assert match(y*x, a*a) == None

def test_match_same_symbol_can_match_identically():
    x = Symbol('x')
    a = Symbol('a')
    assert match(x*x, a*a) == {a: x}

def test_match_symbol_clash():
    x = Symbol('x')
    y = Symbol('y')
    assert match(x*y, x*x) == None

def test_match_symbol_clash_duplicate():
    x = Symbol('x')
    assert match(x*x + x*x, x+x) == {x: x*x}

