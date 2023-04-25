a= int (input("ingrese cantidad de piezas: "))
x=1
b=0
while x<=a:
    b=float(input("ingrese la longitud: "))
    if b<=1.20 and b>=1.30:
        print ("la pieza es apta")
        y=y+1
    x=x+1
print ("la cantidad de piezas aptas son: ",b)
