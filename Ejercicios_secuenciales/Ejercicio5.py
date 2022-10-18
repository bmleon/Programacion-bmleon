"""
5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
# La formula seria (°F − 32) × 5 / 9 = 0 °C, en la formula pone 32ºF pero puede ser cualquier numero

print("Este programa convierte los grados Fahrenheit a grados Celsius")

# Creamos las variables
fahrenheit = float(input("Dame un numero: "))
celsius = (fahrenheit - 32) * 5 / 9

# Mostramos el resultado del cambio
print("El cambio de grados seria: ", celsius)
