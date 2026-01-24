#Operaciones Matemáticas básicas

#Entradas de datos
#Declaracion de variables
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

#Procesos (Calculos u operaciones matematicas y/o logicas)
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1*num2
division = num1/num2
potencia = num1**num2
mod = num1%num2

#Salida de datos (Resultados)
print("El resultado de la suma es: ", suma); #Concatenacion de la suma
print("El resultado de la resta es: ", resta); #Concatenacion de la resta
print("El resultado de la multiplicacion es: " + str(multiplicacion)); # + str(variable) esto es casteo, convertir un tipo de dato en otro
print(f"El resultado de la division es = {division}"); #Interpolacion de cadenas
print("El resultado de la potencia es: ",potencia);
print("El resultado del mod es: ", mod);