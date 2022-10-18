"""
15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
los valores de ambas variables y muestre cuanto valen al final las dos variables.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
print("Programa que cambia el valor de dos variables: ")

# Creamos las variables
a = float(input("Inserta un número para la variable a: "))
b = float(input("Inserta un número para la variable b: "))

# Cambiamos el resultado de las variables
c = a  # Creamos la variable c para guardar el resultado de a
a = b
b = c

# Mostramos el resultado del intercambio
print("El valor de A es: ", a)
print("El valor de B es: ", b)

