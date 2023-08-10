# ejercicio 7
# Comprobar si una cadena contiene al menos una vocal. Solamente mostrar si es True o False

cadena = input("Introduce una cadena de texto: ")
vocales = "aeiouAEIOU"

contiene_vocal = any(vocal in cadena for vocal in vocales)

print(contiene_vocal)

