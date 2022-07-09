# Binary search
target = int(input("Ingre un número: "))
epsilon = 0.01
lower_val = 0.0
upper_val = max(1.0, target)
res = (upper_val + lower_val)/2

while abs(res**2 - target) >= epsilon:
    if res**2 < target:
        print(lower_val, upper_val, res)
        lower_val = res
    else:
        upper_val = res


    res = (upper_val + lower_val)/2

print(f"La raiz cuadrada de {target} es {res}")