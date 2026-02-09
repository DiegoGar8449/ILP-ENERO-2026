#Realizar un programa que realice un cuestionario con las siguientes 12 preguntas, 
#muestre su resultado aciertos / 12 y mostrar la calificación = (aciertos / 12) * 10:

aciertos = 0

respuesta1 = input("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código: " '\n'
"a) IDE     b) Pseudocódigo     c) Compilador     d) ANSI / ISO." "\n"
"Ingrese su respuesta: ")
if (respuesta1 == "b"):
    aciertos += 1
respuesta2 = input("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados." '\n'
"a) Información     b) Datos     c) Programa     d) Código" '\n'
"Ingrese su respuesta: ")
if (respuesta2 == "a"):
    aciertos += 1
respuesta3 = input("3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo. '\n'"
"a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode" '\n'
"Ingrese su respuesta: ")
if (respuesta3 == "c"):
    aciertos += 1
respuesta4 = input("4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema. " '\n'
"a) Proceso     b) Solución     c) Función     d) Algoritmo" '\n'
"Ingrese su respuesta: ")
if (respuesta4 == "d"):
    aciertos += 1
respuesta5 = input("5. Conjunto de elementos que se relacionan para cumplir una función determinada." '\n'
"a) Estructura     b) Datos     c) Operación     d) Sistema" '\n'
"Ingrese su respuesta: ")
if (respuesta5 == "d"):
    aciertos += 1
respuesta6 = input("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina." '\n'
" a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete" '\n'
"Ingrese su respuesta: ")
if (respuesta6 == "d"):
    aciertos += 1
respuesta7 = input("7. Elemento que se usa para almacenar una cantidad donde cambia su valor." '\n'
"a) Constante     b) Variable     c) Librería     d) Tipo de Dato" '\n'
"Ingrese su respuesta: ")
if (respuesta7 == "b"):
    aciertos += 1
respuesta8 = input("8. Conjunto de símbolos, letras, números que no tienen un significado." '\n'
"a) Datos     b) Estructura     c) Información     d) Sistema" '\n'
"Ingrese su respuesta: ")
if (respuesta8 == "a"):
    aciertos += 1
respuesta9 = input("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento." '\n'
"a) Filosofía     b) Sociología     c) Lógica     d) Argumentación" '\n'
"Ingrese su respuesta: ")
if (respuesta9 == "c"):
    aciertos += 1
respuesta10 = input("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto." '\n'
"a) Evento     b) Estándar     c) Calidad     d) Productividad" '\n'
"Ingrese su respuesta: ")
if (respuesta10 == "b"):
    aciertos += 1
respuesta11 = input("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico." '\n'
"a) Estructura     b) Sistema     c) Objeto     d) Virtual" '\n'
"Ingrese su respuesta: ")
if (respuesta11 == "a"):
    aciertos += 1
respuesta12 = input("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar." '\n'
"a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando" '\n'
"Ingrese su respuesta: ")
if (respuesta12 == "c"):
    aciertos += 1

calificacion = (aciertos/12) *10

print("La cantidad de aciertos es: ",aciertos)
print("Su calificación final es: ",calificacion)