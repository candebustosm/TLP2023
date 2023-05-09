import math

n= int (input("Ingrese la cantidad de pares de datos que desea ingresar " ))
count=0

for i in range (n):
    while True:
        try:
            base=float(input("Ingrese la medida de la base del triangulo {}:".format(i+1)))
            altura= float (input("Ingrese la medida de la altura del triangulo{}:".format(i+1)))
            if base <= 0 or altura <= 0:
                raise ValueError
            break
        except ValueError:
            print ("Error: Ingrese un numero positivo para la base y altura del triangulo ")
    superficie= (base*altura)/2
    print ("El triangulo {} tiene una base de {} y una altura de {} . Su superficie es de {} .".format(i+1, base, altura, superficie))

    if superficie > 12:
        count +=1

print ("La cantidad de triangulos cuya superficie es mayor a 12 es: {}".format(count))

            
