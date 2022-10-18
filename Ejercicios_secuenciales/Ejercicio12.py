"""
12. Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la
distancia entre ellos.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
# d(A,B) = sqrt(x_2-x_1)^2+(y_2-y_1)^2
# importamos la función math para la raíz cuadrada
import math
print("Dime las coordenadas del punto 1:")
x1 = int(input())
y1 = int(input())
print("Dime las coordenadas del punto 2:")
x2 = int(input())
y2 = int(input())
distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("Distancia:", distancia)
