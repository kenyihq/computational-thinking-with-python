# Float representation
x = 0.0
for i in range(10):
    x += 0.1
    print(x)

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')

# Floats aren´t exact

x = 0.0
for i in range(10):
    x += 0.1
    print(x)

if x > 0.999 and x  < 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')