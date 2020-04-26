lista = [1,"dos",3]

buscar = 3

print (buscar in lista) #busca 1 en la lista

print(lista.index(buscar)) #buscar el indice

#BUSCAR numero en lista y su indice

lis =[1,2,4,"j",3,5]
num = 3
if num in lis:
    print ("EL numero",num,"fue encontrado en indice",lis.index(num))
else:
    print ("NO SE ENCONTRO")

#LISTA REPETIDA
li = [1,2,3,4]
print (li)
li.append(3)
print (li)

#BUSCAR CANTIDAD DE VESES REPETIDAS

print (li.count(3)," veses se repite 2")

#INSERTAR EN UN INDICE O REMPLAZAR

li.insert(0,"Lista")
print(li)

#Extender cada elemento 
iterable = "Entex"
tupla = (9,8,7,6,5)
li.extend(iterable)
li.extend(tupla)
print(li)

#METODO POP
li.pop(2)
print(li)

#BORRAR EN LISTA
#li.remove(2)
#print(li)

#invertir
li.reverse()
print(li)
