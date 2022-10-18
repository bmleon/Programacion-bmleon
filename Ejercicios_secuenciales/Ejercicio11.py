"""11. Pide al usuario dos números y muestra la "distancia" entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
# La formula de la distancia es D=v*t
velocidad = float(input("Dame una velocidad: "))
tiempo = float(input("Dame un tiempo: "))

# Calculamos la distancia
distancia = velocidad * tiempo
# Mostramos el resultado
print("El resultado de la distancia seria: ", distancia)
