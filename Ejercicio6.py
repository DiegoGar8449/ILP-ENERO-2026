#6. Pedir un número y decir si es par o impar.

#Entrada de datos
numero = int(input("Ingrese un numero: "))

#Proceso de datos
par = numero/2
impar = numero%2
if (impar == 1):
    print("El numero es impar")
else: print("El numero es par")

#Salida de datos
#print("El numero es par si fue divisible entre 2: ",par)
#print("El numero es impar si el resultado es 1 [Residuo]: ",impar)