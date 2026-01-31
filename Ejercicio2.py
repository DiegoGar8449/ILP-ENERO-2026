#Calcular el area y perimetro de un circulo

#Entrada de datos
radio = float(input("Ingrese el radio del circulo: "))
PI = 3.1416

#Proceso
area = PI*radio**2
perimetro = 2*(PI*radio)

#Salida de datos
print("El area del circulo es: ",area)
print("El perimetro del circulo es: ",perimetro)