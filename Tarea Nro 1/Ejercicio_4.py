# Ejercicio N° 4

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la
#<n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
#introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
#respectivamente.

n = int(input("Introduce el primer número (n): "))
m = int(input("Introduce el segundo número (m): "))

cociente = n // m
resto = n % m

print(f"{n} entre {m} da un cociente = {cociente} y un resto = {resto}")
