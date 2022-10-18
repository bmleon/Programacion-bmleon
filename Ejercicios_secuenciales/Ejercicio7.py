"""
7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""

# Creamos las variables
minutos_iniciales = int(input("Inserta los minutos que quieres cambiar: "))

# Hacemos el cambio de horas y minutos
horas = minutos_iniciales // 60
minutos_finales = minutos_iniciales % 60

# Mostramos el resultado
print("Las horas son ", horas, "los minutos son ", minutos_finales)
