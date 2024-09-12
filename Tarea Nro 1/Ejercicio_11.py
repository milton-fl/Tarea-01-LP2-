# Ejercicio N° 11

#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre
#por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase: ")

letra = input("Introduce una letra: ")

if len(letra) != 1:
    print("Por favor, introduce solo una letra.")
else:
    conteo = frase.count(letra)

    print(f"La letra '{letra}' aparece {conteo} veces en la frase.")
