# ejercicio 6
# Verificar si un numero es par y positivo. Solamente mostrar si es True o False

numero = int(input("ingrese un numero:"))

es_par_y_positivo = numero % 2 == 0 and numero > 0

print(es_par_y_positivo)
