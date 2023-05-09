pares = 0
impares = 0


cantidad_numeros = int(input("Ingrese la cantidad de números a ingresar: "))


contador = 0
while contador < cantidad_numeros:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1


print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
