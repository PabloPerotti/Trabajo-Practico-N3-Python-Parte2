# ejercicio 8
# En un laboratorio se debe trabajar en condiciones ideales. Estas son una temperatura entre 20ºC y 25ºC
# y humedad entre 70% y 90%. Antes de comenzar con su trabajo el empleado debe ingresar en el sistema tanto 
# la temperatura y humedad que se registran en el laboratorio y este
# le debe devolver True o False segun se cumplan las condiciones ideales.

temperatura = float(input("Introduce la temperatura (en ºC): "))
humedad = float(input("Introduce la humedad (%): "))

temperatura_ideal = 20 <= temperatura <= 25
humedad_ideal = 70 <= humedad <= 90

condiciones_ideales = temperatura_ideal and humedad_ideal

print(condiciones_ideales)
