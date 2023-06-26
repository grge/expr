from expr import Symbol, Function, create_constant


zero = create_constant('zero', repr='0')

print(zero + 1)
