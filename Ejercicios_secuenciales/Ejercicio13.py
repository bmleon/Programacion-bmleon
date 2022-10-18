"""13. Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
# Primero hacemos la raíz cuadrada
import math

# Calculamos las raíces
num = int(input("Dime el número:"))
print("Raíz cuadrada:", math.sqrt(num))
print("Raíz cúbica:", num ** (1 / 3))
