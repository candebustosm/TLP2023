x=1
y=0
z=0
while x<10:
    nota=int(input("ingrese la nota: "))
    if nota>=7:
        y=y+1
    else :
        z=z+1
    x=x+1
print ("la cantidad de notas mayores a 7 son " ,y)
print ("la cantidad de notas menores a 7 son " ,z)

