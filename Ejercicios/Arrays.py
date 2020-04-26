lis = [2,"tres",True,["uno",10,"Hola"],2,"Miau"]

rec = lis[2]
print(lis)
print(rec)
print(lis[3][2]) #Acceder a un lista dentro de una lista 

lis[0] = "zero"
lis2 = lis[1:3]#copiar datos de otro array a un nuevo array
lis3 = lis[0::2]#Va intercalando dependiendo de lo deseado
lis24 = lis[1:3]#


print(lis)
print(lis2)
print(lis3)
lis[0:3] = [4,4,5] #Intercambiar datos del arrays 
print(lis)

lis5 = lis[-1] #Acede desde la ultima posicion del array

print(lis5) 
