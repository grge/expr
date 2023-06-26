from expr import Symbol
from rewrite import rewrite

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')

simplification_rules = [
    # Combine like terms
    (x + x, 2 * x),
    (x - x, 0),
    (x * x, x**2),

    
    # Distributive property
    (x * (y + z), x * y + x * z),
    (x * (y - z), x * y - x * z),
    ((y + z) * x, y * x + z * x),
    ((y - z) * x, y * x - z * x),
    
    # Multiplication with 0 and 1
    (x * 0, 0),
    (0 * x, 0),
    (x * 1, x),
    (1 * x, x),
    
    # Division by 1 and by the same term
    (x / 1, x),
    (x / x, 1),
    
    # Exponentiation
    (x ** 0, 1),
    (x ** 1, x),
    
    # Negation
    (x + (-x), 0),
    (-x + x, 0),
]

# Example expression to simplify
expr = (x * x + x * y) + (x * x - x * y)

# Apply the simplification rules
simplified_expr = rewrite(expr, simplification_rules, max_rewrites=22)
print(simplified_expr)
