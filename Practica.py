def main():
    print ("Convierte medidas inglesas a sistema metrico")
    millas = input("Cuántas millas?: ")
    pies = input("Y cuántos pies?: ")
    pulgadas = input("Y cuántas pulgadas?: ")
    metros = (1 * millas) + (1 * pies) + (4 * pulgadas)
    print ("La longitud es de ", metros, " metros")

main()
