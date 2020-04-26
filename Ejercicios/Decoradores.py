loggeado = True
usuario = "HOOla"
def admin(f):
    def comprobar(*args,**kwargs):
        if loggeado:
            f(*args,**kwargs)
        else:
            print("No tienes permisos de ejecutar",f.__name__)
    return comprobar


def decorador (funcion):
    def funcionDecorada(*args,**kwargs):
        print("Funcion ejecutada",funcion.__name__)
        funcion(*args,**kwargs)

    return funcionDecorada

#(decorador(resta)(5,3))

@admin
@decorador

def resta(n,m):
    print(n-m)

#decorador

resta(5,3)




