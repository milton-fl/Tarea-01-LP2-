# Ejercicio N° 8

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo, de altura el número introducido.

altura = int(input("Introduce un número entero para la altura del triángulo: "))

for i in range(1, altura + 1):
    print('*' * i)
