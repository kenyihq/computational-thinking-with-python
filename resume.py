def enumeration(target):
    res = 0

    while res ** 2 < target:
        res += 1

    if res**2 == target:
        solution = f"La raiz cuadrada de {target} es {res}"
    else:
        solution = f"{target} no tiene raiz cuadrada exacta"

    return solution

def aproximation(target):
    import time

    start_time = time.time()

    epsilon = 0.01
    step = epsilon**2
    res = 0.0

    while abs(res**2 - target) >= epsilon and res <= target:
        #print(f"")
        res += step

    if abs(res**2 - target) >= epsilon:
        solution = f"No se encontró la raiz cuadrada de {target}"
    else:
        solution = f"La raiz cuadrada de {target} es {res}"
        solution += f"\nTiempo de ejecucucion: {round((time.time() - start_time), 2)} segundos"
    
    return solution

def binary_search(target):
    epsilon = 0.01
    lower_val = 0.0
    upper_val = max(1.0, target)
    res = (upper_val + lower_val)/2

    while abs(res**2 - target) >= epsilon:
        if res**2 < target:
            print(f"Valor minimo: {lower_val} | Valor máximo: {upper_val} | Respuesta {res}")
            lower_val = res
        else:
            upper_val = res


        res = (upper_val + lower_val)/2

    solution = f"La raiz cuadrada de {target} es {res}"

    return solution

def print_menu():
    print("*"*30)
    print("* ALGORITMOS DE APROXIMACION *")
    print("*" + " "*28 + "*")
    print("* 1. Enumeración             *")
    print("* 2. Aproximación            *")
    print("* 3. Busqueda binaria        *")
    print("*"*30)

def run():

    print_menu()
    option = input("Opción: ")

    try:
        option = int(option)

        while option > 0 and option < 4:
            target = int(input("Ingrese un número entero: "))
            if option == 1:
                enumeration(target)
                print(enumeration(target))
            elif option == 2:
                aproximation(target)
                print(aproximation(target))
            elif option == 3:
                binary_search(target)
                print(binary_search(target))
            break

        else:
            print("\n" + "-"*30)
            print("Elija una opción válida")
            print("-"*30 + "\n")
            run()
    except ValueError:
        print("\n" + "-"*30)
        print("Solo ingrese números")
        print("-"*30 + "\n")
        run()

if __name__ == "__main__":
    run()