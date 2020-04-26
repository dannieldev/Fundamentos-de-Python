#remplasa los metodos de filtro y busqueda
l = [1,3,4,6,-2]
#filtra la lista
l2 = [num for num in l if num >0]


print(l)
print(l2)

s = ["H","O","L","A"]
l3 = [c* num for c in s for num in l if num > 0]


print (l3)
