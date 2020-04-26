nom = input("Bienvenido cual es tu nombre ")

hola(nom)

for x in [1,3,9,27,2]:
    print (x * x)

print("\n")
for x in range(10,20):
    print (x)
print("\n")


    
print("Saluda a 5 amigos")

for x in range(1,6):
    saludar()

print ("saluda de nuevo")


n = input("A cuantos amigos quieres saludar")

for x in range(int(n)):
    saludar()



#obtiene nombres y los saludas
def saludar():
    fa = input("Nombre de amigo ")
    print ("Saludos ",fa)
    

def hola(nom):
    print("Bienvenido ",nom)
    
