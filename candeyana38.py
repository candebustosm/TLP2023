n = int(input("Ingrese la cantidad de triángulos que desea analizar: "))


equilateros = 0
isoceles = 0
escalenos = 0


for i in range(n):
    print("Ingrese los lados del triángulo", i+1)
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))
    
    
    if a == b == c:
        print("El triángulo", i+1, "es equilátero")
        equilateros += 1
    elif a == b or a == c or b == c:
        print("El triángulo", i+1, "es isósceles")
        isoceles += 1
    else:
        print("El triángulo", i+1, "es escaleno")
        escalenos += 1

# Mostramos los resultados
print("Cantidad de triángulos equiláteros:", equilateros)
print("Cantidad de triángulos isósceles:", isoceles)
print("Cantidad de triángulos escalenos:", escalenos)
