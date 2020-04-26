li = [1,3,5,-2]
lo = [5,4,5,3]
s = "Hola mundo"

ss = lambda n,m: n+m

print (map(ss,li,lo))
print (filter(lambda n: n=="o",s))
#print (reduce(ss,lo))

print (ss(4,2)) #suma con la funcion lambda
