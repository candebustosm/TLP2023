num=0
y=0
z=0
for x in range (10) :
   num= int (input("Ingrese un numero " ))
   if num%3==0:
       y=y+1
   if num%5==0: 
        z=z+1
print ("Los numeros multiples de 3 son " ,y)
print ("Los numeros multiples de 5 son ", z)
