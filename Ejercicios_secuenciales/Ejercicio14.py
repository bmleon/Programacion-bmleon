"""Ejercicio14: Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""

print("Este programa obtiene el invertido de un número dado")

# Creamos las variables
num = int(input("Dime un número de dos cifras: "))
numero1 = num // 10
numero2 = num % 10

# Hacemos el cambio
invertido = numero2 * 10 + numero1

# Mostramos el resultado
print("Mostramos el número invertido: ", invertido)
