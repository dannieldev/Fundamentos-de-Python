class UnoError(Exception):
    def __init__(self,valor):
        self.valorError = valor
    def __str__(self):
        print("no se puede dividir entre 1 el numero",self.valorError)

print("Hola")

e= 5
h=1

n=2
try:
    print(0/n)
    if(n==2):
        raise UnoError(e) #Lanzar el error creado
except UnoError:
    print("Error creado")
except (TypeError,):
    print("Error en tipo de dato")
except (NameError):
    print("Variable no existe")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print("No hubo error")
finally:
    print("Me ejecuto pasae lo que pase")
    
print("Adios")



        


