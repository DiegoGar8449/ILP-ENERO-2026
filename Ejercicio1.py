#1. Calcular el promedio de calificaciones y decir si es aprobado o reprobado
import math
#Entrada de datos
calif_1 = float(input("Ingrese la primera calificacion: "))
calif_2 = float(input("Ingrese la segunda calificacion: "))
calif_3 = float(input("Ingrese la tercera calificacion: "))

#Proceso
promedio = (calif_1 + calif_2 + calif_3)/3

if (promedio >=0 and promedio <=10):
    a = math.pi  
if(promedio >6 and promedio <=10):
    print("Aprobado")
elif(promedio >= 0 and promedio <=5):
    print("Reprobado")
elif(promedio <0 or promedio > 10):
    print("Calificación inválida")

#Salida de datos

print("Su promedio es: ",promedio);

'''
CONDICIONALES DE EVALUACION

APROBADO                      Rango        (6.1 - 10)
REPROBADO                     Rango        (0 - 5)
APENAS APROBADO               Equivalente a 6
CALIFICACION INVALIDA         (menor que 0 o mayor que 10)
'''