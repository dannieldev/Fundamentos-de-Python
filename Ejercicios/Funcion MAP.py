def operador(n,m):
    if n==None or m == None:
        return 0
    
    return n+m

li = [1,2,3,4]
tu = (9,8,7,6)

re = map(operador,li,tu)

print(li)
print(tu)
print(re)
