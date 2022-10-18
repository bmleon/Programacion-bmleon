"""
17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra
ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
hora_partida = int(input("Hora de salida:"))
minutos_partida = int(input("Minutos de salida:"))
segundos_partida = int(input("Segundos de salida:"))
segundos_viaje = int(input("Tiempo que has tardado en segundos:"))

# Convierto la hora de salida a segundos
segundos_iniciales = hora_partida * 3600 + minutos_partida * 60 + segundos_partida

# Le sumo los segundos que he tardado
segundos_finales = segundos_iniciales + segundos_viaje

# Convierto los segundos totales a hora, minutos y segundos
hora_llegada = segundos_finales // 3600
minutos_llegada = (segundos_finales % 3600) // 60
segundos_llegada = (segundos_finales % 3600) % 60

# Muestro la hora de llegada
print("Hora de llegada")
print(hora_llegada, ":", minutos_llegada, ":", segundos_llegada)
