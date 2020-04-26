class Prueva (object):
    def __init__(self):
        self.__privado = "Soy Privado"
        #Los 2 guiones representan a algo privado  
        self.privado = "Soy Publico"

    def __metodoPrivado(self):
        return ("Soy Privado")

    def metodoPublico(self):
        print ("Soy Publico")

    def getPrivado(self):
        return (self.__privado)

    def setPrivado(self,valor):
        self.__privado = valor

obj = Prueva()

#print (obj.privado)
#print (obj.__privado)

obj.setPrivado("Valor Agregado")
print(obj.getPrivado())
#obj.metodoPrivado()
#obj.__metodoPrivado()
