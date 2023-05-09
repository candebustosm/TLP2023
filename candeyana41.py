edadesmanana = []
for i in range(5):
    edad = int(input("Ingrese la edad de un estudiante del turno mañana: "))
    edadesmanana.append(edad)

edadestarde = []
for i in range(6):
    edad = int(input("Ingrese la edad de un estudiante del turno tarde: "))
    edadestarde.append(edad)

edadesnoche = []
for i in range(11):
    edad = int(input("Ingrese la edad de un estudiante del turno noche: "))
    edadesnoche.append(edad)


promediomanana = sum(edadesmanana) / len(edadesmanana)
promediotarde = sum(edadestarde) / len(edadestarde)
promedionoche = sum(edadesnoche) / len(edadesnoche)


print("Promedio de edad del turno mañana:", promediomanana)
print("Promedio de edad del turno tarde:", promediotarde)
print("Promedio de edad del turno noche:", promedionoche)


if promediomanana > promediotarde and promediomanana > promedionoche:
    print("El turno mañana tiene el promedio de edad mayor.")
elif promediotarde > promediomanana and promediotarde > promedionoche:
    print("El turno tarde tiene el promedio de edad mayor.")
else:
    print("El turno noche tiene el promedio de edad mayor.")
    
