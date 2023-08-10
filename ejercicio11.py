###########################################################################
##### 🚨Estos ejercicios deben realizarse sin estructuras condicionales🚨 #####
# ejercicio 4
# Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
# -Si los dos números son iguales
numero1 = input("Ingresa el primer numero: ")
numero2 = input("Ingresa el segundo numero: ")
respuesta = numero1 == numero2
print(respuesta)

# -Si los dos números son diferentes
numero1 = input("Ingresa el primer numero: ")
numero2 = input("Ingresa el segundo numero: ")
respuesta = numero1 != numero2 
print(respuesta)

# -Si el primero es mayor que el segundo
numero1 = input("Ingresa el primer numero: ")
numero2 = input("Ingresa el segundo numero: ")
respuesta = numero1 > numero2 
print(respuesta)

# -Si el segundo es mayor o igual que el primero
numero1 = input("Ingresa el primer numero: ")
numero2 = input("Ingresa el segundo numero: ")
respuesta = numero1 <= numero2 
print(respuesta)