#clases
print("CLASES")
class Humano:
    def __init__(self,edad,masa):
        self.edad = edad
        self.peso = masa #masa el atribulo solo se usa dentro de la clase pero peso es como se manda a llamar 
        print("hoy un nuevo objeto")

    def hablar(self,mensaje,mas):
        print (mensaje,mas)

    def escuchar(self,oido):
        print(oido)
    

pedro = Humano(21,120)
raul = Humano(18,130)
sentido = Humano(20,250)

raul.hablar('hola,Pedro!','texto de mas')

print ("hola soy francisco y tengo",raul.edad,'y pesa',raul.peso)
print ("hola soy francisco y tengo",pedro.edad,'y pesa',pedro.peso)
print ("el peso de sentido es de",sentido.peso)

pedro.hablar('pedro tiene,piojos','hola')

sentido.escuchar('te escucho')


import time


#herencia
print("\n")
time.sleep(2)
print("HERENCIA")
class IngSistemas(Humano):
    def programar(self,lenguaje):
        self.lenguaje = lenguaje
        print ('Voy a programar en',lenguaje)

class LicDerecho(Humano):
    def __init__(self,escuela): #sobreescribir funsion
        self.estudio = escuela
        print('Lic, en derecho egresado de: ',escuela)
    def estudiarCaso(self,de):
        print ('Debo estudiar el caso de',de)
    
progra = IngSistemas(25,130)
lice = LicDerecho('España')

progra.programar('Python')
lice.estudiarCaso('Pedro')
print('programador edad ',progra.edad,' peso ',progra.peso,'y programo en',progra.lenguaje)
print('lic Derecho estudio en ',lice.estudio)

#herencia Multiple
print("\n")

time.sleep(2)
print("HERENCIA MULTIPLE")

class estudioso(LicDerecho,IngSistemas):
    pass  #operación nula ,relleno temporal

pablo = estudioso('El Salavdor')


pablo.hablar('Hola soy de herencia multiple','multiple')
pablo.programar('C++')
pablo.estudiarCaso('Juan')

