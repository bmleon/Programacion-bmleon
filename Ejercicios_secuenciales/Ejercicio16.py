"""16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre
los dos vehículos (km) y sus respectivas velocidades (km/h)
y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""

# Creamos las variables de velocidad y distancia
velocidad1 = float(input("Dime la velocidad del coche 1 (km/h):"))
velocidad2 = float(input("Dime la velocidad del coche 2 (km/h):"))
distancia = float(input("Dime la distancia entre los coches (km):"))

tiempo = distancia / abs(velocidad1 - velocidad2)
tiempo = tiempo * 60

# Mostramos el resultado
print("Lo alcanza en", tiempo, "minutos.")
