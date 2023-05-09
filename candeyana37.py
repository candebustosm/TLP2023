num = int(input("Ingrese el número de la tabla de multiplicar que desea mostrar: "))

for i in range(1, 13):
    print("{} x {} = {}".format(num, i, num * i))
    
