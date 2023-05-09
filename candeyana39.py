n = int(input("Ingrese la cantidad de puntos que desea analizar: "))


cuadrante_1 = 0
cuadrante_2 = 0
cuadrante_3 = 0
cuadrante_4 = 0


for i in range(n):
    print("Ingrese las coordenadas del punto", i+1)
    x = float(input("Coordenada x: "))
    y = float(input("Coordenada y: "))
    
    
    if x > 0 and y > 0:
        cuadrante_1 += 1
    elif x < 0 and y > 0:
        cuadrante_2 += 1
    elif x < 0 and y < 0:
        cuadrante_3 += 1
    elif x > 0 and y < 0:
        cuadrante_4 += 1


print("Cantidad de puntos en el primer cuadrante:", cuadrante_1)
print("Cantidad de puntos en el segundo cuadrante:", cuadrante_2)
print("Cantidad de puntos en el tercer cuadrante:", cuadrante_3)
print("Cantidad de puntos en el cuarto cuadrante:", cuadrante_4)
