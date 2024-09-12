# Ejercicio N° 3

#Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que
#se le hace por no ser fresca y el coste final total.

precio_barra = 2.5

descuento = 0.60

barras_no_frescas = int(input("Introduce el número de barras no del día vendidas: "))

precio_sin_descuento = barras_no_frescas * precio_barra
precio_con_descuento = precio_sin_descuento * (1 - descuento)

print(f"Precio habitual de una barra de pan: {precio_barra}€")
print(f"Descuento por no ser fresca: {descuento * 100}%")
print(f"Coste final total: {precio_con_descuento:.2f}€")
