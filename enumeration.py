# Enumeration

tarjet = int(input("Ingrese un número entero: "))
res = 0

while res ** 2 < tarjet:
    res += 1

if res**2 == tarjet:
    print(f"La raiz cuadrada de {tarjet} es {res}")
else:
    print(f"{tarjet} no tiene raiz cuadrada exacta")