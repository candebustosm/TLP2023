positivos = 0
negativos = 0
multiplos15 = 0
acumuladopares = 0


for i in range(10):
    valor = int(input("Ingrese un valor entero: "))
    
   
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    
   
    if valor % 15 == 0:
        multiplos15 += 1
    
    
    if valor % 2 == 0:
        acumuladopares += valor


print("Cantidad de valores ingresados positivos:", positivos)
print("Cantidad de valores ingresados negativos:", negativos)
print("Cantidad de múltiplos de 15:", multiplos15)
print("Acumulado de valores ingresados pares:", acumuladopares)
