text = "hola papa como la pasas"

print(text)
print("\n")
#funsion de numeros de caracteres de cadena
print (len(text))

#contar el numero de veses que se repite lo que nosotros designemos
print (text.count("A"))

#contar entre los caracteres
print (text.count("o",0,3))
print (text.count("a",3,9))
print (text.count("a",21))

#Mayusculas y minusculas

print (text.lower())

print (text.upper())

#remplasar
#cantidad de veses al renplasar
print (text.replace('o','x',2))

#cortar cadena
print (text.split("a"))
print (text.split("a",3))

#Buscar en la cadena
print (text.find("a"))

#Buscar de atras para adelante
print (text.rfind("a"))

#TUPLA Unidas
t =("H","O","L","A")
s =","

print (s.join(t))
print (type(s.join(t)))
