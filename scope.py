a = "Soy un a varaible global"

def mi_funcion():
    a = "Soy una variable local y le pertenesco a mi_funcion()"


def otra_funcion():
    global a
    a = "Soy una varable local y con el key 'global' soy una variable global"