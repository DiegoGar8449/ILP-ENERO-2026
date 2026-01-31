#4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

#Entrada de datos
k1 = float(input("Kelvin a Celcius - Ingrese los grados Kelvin: "))             #1
f1 = float(input("Fahrenheit a Celcius - Ingrese los grados Fahrenheit: "))     #2
c1= float(input("Celcius a Kelvin - Ingrese los grados Celcius: "))             #3
k2 = float(input("Kelvin a Fahrenheit - Ingrese los grados Kelvin: "))          #4
f2 = float(input("De Fahrenheit a Kelvin - Ingrese los grados Fahrenheit: "))   #5
c2 = float(input("De Celcius a Fahrenheit - Ingrese los grados Celcius: "))     #6

#Proceso de datos
kc = k1 - 273.15            #1
fc = (5*(f1-32))/9          #2
ck = c1+273.15              #3
kf = (9*(k2-273.15))/5+32   #4
fk = (5*(f2-32))/9+273.15   #5
cf = (9*c2)/5+32            #6

#Salida de datos
print("Los grados de Kelvin a Celcius son: ",kc)      #1
print("Los grados de Fahrenheit a Celcius son: ",fc)  #2
print("Los grados de Celcius a Kelvin son: ",ck)      #3
print("Los grados de Kelvin a Fahrenheit son: ",kf)   #4
print("Los grados de Fahrenheit a Kelvin son: ",fk)   #5
print("Los grados de Celcius a Fahrenheit son: ",cf)  #6