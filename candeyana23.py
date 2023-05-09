empleadosentre100y300 = 0
empleadosmasde300 = 0
totalsueldos = 0

sueldo = float(input("Ingrese el sueldo del empleado (ingrese un número negativo para finalizar): "))
while sueldo >= 0:
    totalsueldos += sueldo
    if sueldo >= 100 and sueldo <= 300:
        empleadosentre100y300 += 1
    elif sueldo > 300 and sueldo <= 500:
        empleadosmasde300 += 1
    sueldo = float(input("Ingrese el sueldo del empleado (ingrese un número negativo para finalizar): "))


print(f"La empresa tiene {empleadosentre100y300} empleados que cobran entre 100 y 300 dólares, y {empleadosmasde300} empleados que cobran más de 300 dólares.")
print(f"El total de sueldos que gasta la empresa es de {totalsueldos} dólares.")
