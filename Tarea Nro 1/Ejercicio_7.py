# Ejercicio N° 7

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Introduce un número entero positivo: "))

if numero >= 0:
    
    cuenta_atras = ", ".join(map(str, range(numero, -1, -1)))
    print(cuenta_atras)
else:
    print("El número debe ser un entero positivo.")
