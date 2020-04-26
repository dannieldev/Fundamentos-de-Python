try:
    f = open("nuevo.txt","w")
    print("Archivo abierto")
except:
    f ="Error"
    print("Error al abrir archivo")

#escribe al final del archivo
f.write("Este es mi primer bloque")

#bit desde el principio
f.seek(11)

#bit desde el final
f.seek(0,2)
print(f.tell)

agregar =["hola \n","Mundo","Hellow"]

f.write("intruso")

f.close()
if not f.closed:
    f.writelines(agregar)
