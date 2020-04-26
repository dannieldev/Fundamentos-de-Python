
try:
    f = open("Texto.txt","w")
    print("Archivo abierto")
except:
    f ="Error"
    print("Error al abrir archivo")
else:
    f.close()
    print(f)
print(f)
