import time

start_time = time.time()

target = int(input("Ingresa un número entero: "))

epsilon = 0.01
step = epsilon**2
res = 0.0

while abs(res**2 - target) >= epsilon and res <= target:
    #print(f"")
    res += step

if abs(res**2 - target) >= epsilon:
    print(f"No se encontró la raiz cuadrada de {target}")
else:
    print(f"La raiz cuadrada de {target} es {res}")
    print(f"Tiempo de ejecucucion: {time.time() - start_time}")