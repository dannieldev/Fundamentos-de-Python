s = ('H','o','l','a','_','M','u','n','d','o')

def concatenar(a,b):
    return a+b

sr = reduce(concatenar,s)
    
print(type(sr))
print(sr)
