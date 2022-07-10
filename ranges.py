# Range
def my_range(sr, en, st=1):
    """Crea un rango de números

        sr, en, st <- int
        sr: start
        en: end
        st: step
    """
    r = range(sr, en, st)
    return list(r)


print(my_range(1,100,2))