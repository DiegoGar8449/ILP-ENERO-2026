#7. Pedir el nivel del agua en metros de una cisterna

nivel_agua = int(input("Ingrese el nivel de agua de su cisterna: "))
if (nivel_agua > 6):
    print("Desbordamiento de agua en la cisterna")
elif(nivel_agua == 6):
    print("Apagar bomba")
elif(nivel_agua >= 4 and nivel_agua < 6):
    print("Desacelerar bomba")
elif(nivel_agua >=2 and nivel_agua <= 4):
    print("Bomba trabajando")
elif(nivel_agua >= 0 and nivel_agua <= 2):
    print("Acelerar bomba de agua")
elif(nivel_agua == 0):
    print("Encender bomba")
elif(nivel_agua < 0):
    print("Fuga en cisterna")
else: print("Nivel no válido")