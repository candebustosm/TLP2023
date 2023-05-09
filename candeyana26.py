lista1 = []
lista2 = []


contador = 0
while contador < 15:
    valor = int(input("Ingrese un valor para la primera lista: "))
    lista1.append(valor)
    contador += 1


contador = 0
while contador < 15:
    valor = int(input("Ingrese un valor para la segunda lista: "))
    lista2.append(valor)
    contador += 1


suma1 = sum(lista1)
suma2 = sum(lista2)


if suma1 > suma2:
    print("La lista 1 tiene un valor acumulado mayor.")
elif suma1 < suma2:
    print("La lista 2 tiene un valor acumulado mayor.")
else:
    print("Ambas listas tienen el mismo valor acumulado.")
    
