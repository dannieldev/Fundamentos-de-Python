try:
    f = open("new.txt","r")
    print("Archivo")

except:
    exit()
    print("Error")

#leer archivo
#print(f.read())
#rint(f.read(50))
#print("Nueva linea",f.readline())

while True:
    print(f.readline())
    if f.readline() == "":
        break
    
#leer cada linea
lineas = f.readlines()
#print(lineas)

for l in lineas:
    print("=>",l,"\n\n")

