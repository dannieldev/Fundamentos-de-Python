valor = input()

print(valor)
print(type(valor))


try:
    valo = input()
    valo = int(valo)
except: #si no es un numero lanza except
    print("Esto no es un numero")
else:
    print(valo)

