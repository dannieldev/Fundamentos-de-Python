dicionario = {
    "redes_sociales":['Twitter','Facebook','LinkedIn'],
    3:"Tres",
    "Hola":"Mundo",
    "eli":"elininame"
}

print (dicionario)
print (dicionario.pop(3))

del(dicionario["eli"])
print (dicionario)

dicionario.clear()

print (dicionario)

dicionario["clave_nueva"] = "Valor"

print (dicionario)


copidic2 = dicionario.copy()

print(copidic2)




