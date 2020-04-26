def prueba(f):
    return f() #los parentesis ejecutan la funsion reglesa el valor de la funcion

def porEnviar():
    return 2+2

print (prueba(porEnviar))

#Operaciones
def seleccion(operacion):
    
    def suma(n,m):
        return n+m
    def resta(n,m):
        return n-m
    def division(n,m):
        return n/m
    def multiplicacion(n,m):
        return n*m
    
    if operacion == "suma":
        return suma
    elif operacion == "resta":
        return resta
    elif operacion == "division":
        return division
    elif operacion == "multi":
        return multiplicacion

fGuardada = seleccion("division")
print (fGuardada(122,12))
rets = seleccion("resta")
print (rets(10,5))
