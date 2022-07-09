def fibonnacci(n):
    """Calcula Fibonnacci

    n int > 0
    return n-1 + n+1    
    """
    if n == 0 or n == 1:
        return 1

    return fibonnacci(n-1) + fibonnacci(n-2)


def fibonnacci_sin_recursividad(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]

n = int(input("Ingres un número: "))
print(fibonnacci(n))
print(fibonnacci_sin_recursividad(n))