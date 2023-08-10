# ejercicio 3: determinar mentalmente los resultados anotarlos en un papel y luego comprobar ejecutando el programa.
expresion1 = 8 * 4 and 6 > 3 and 34 >= 33
print(expresion1)                                               #true
expresion2 = not 4 > 5 or 5 ** 2 and 6 != 3
print(expresion2)                                               #true
expresion3 = 43 + (22 > 4)
print(expresion3)                                               #44
expresion4 = not 43 or 99 >= 999
print(expresion4)                                               #false
expresion5 = (not 43 or 99 >= 999) and 2 ** 2 or (4 != 43 and "Python" > "Python Recargado")
print(expresion5)                                               #false
expresion6 = 6 and 6 + 34
print(expresion6)                                               #40
expresion7 = 0.0 and 6 + 34
print(expresion7)                                               #0.0
expresion8 = not 0.0 and 5 + 5
print(expresion8)                                               #10
expresion9 = "23" == "23" and 34 >= 34 or (241 < 98 or 436 <= 1988) and not 987 > 76 
print(expresion9)                                               #true