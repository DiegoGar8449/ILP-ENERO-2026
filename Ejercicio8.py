#8. Calcular la nómina para un empleado en el mes de Enero del 2026 conociendo su pago por día de $300.

dias_laborales = int(input("Ingrese los dias que labora: "))
pago_dia = float(input("Ingrese su pago por dia: "))


pago_base = dias_laborales * pago_dia
iva_trasladado = 0.16 * pago_base
iva_retenido = (2/3)*iva_trasladado
isr = 0.10*pago_base
subtotal = pago_base + iva_trasladado
salario_neto = subtotal - iva_retenido - isr

print("El pago por día es: ",pago_dia)
print("El pago base es: ",pago_base)
print("El iva trasladado es: ",iva_trasladado)
print("El iva retenido es: ",iva_retenido)
print("El isr es: ",isr)
print("El subtotal es: ",subtotal)
print("El salario neto es: ",salario_neto)