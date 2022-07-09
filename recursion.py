# Recursividad

"""
    Una funcion se llama a si misma

    Ejemplo:
    Factoriales:
        n! = n * (n-1)!

        4! = 4 * (3!)
        3! = 3 * (2!)
        2! = 2 * (1!)
        1! = 1

        !4 = 4*3*2*1

"""


def factorial(n):
    """Calcula el factorial de n

    n int > 0
    return n!    
    """
    print(n)
    if n == 1:
        return n

    return n * factorial(n - 1)


n = int(input("Escribe un entero: "))

print(factorial(n))