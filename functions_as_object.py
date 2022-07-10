from unittest import result


def al_cuadradro(n):
    return n**2


def duplicar(n):
    return n*n

def operaciones(operacio, n):
    resultado = []
    for i in n:
        r = operacio(i)
        resultado.append(r)
    return resultado


print(operaciones(duplicar, [1,2,3,4,5,6,7,8,9]))


def dup(n): return n*n

