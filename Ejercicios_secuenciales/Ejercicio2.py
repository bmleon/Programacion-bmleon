"""
2. Calcular el perímetro y área de un rectángulo dada su base y su altura.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
# Creamos las variables que usaremos
altura = int(input("introduce la altura: "))
base = int(input("introduce la base: "))
# La formula para calcular el perímetro es
Perimetro = (2 * base) + (2 * altura)

# Para calcular el área de la base
area = base * altura
# Mostramos el resultado del perímetro y el área
print("El perímetro del rectángulo es ", Perimetro, "y el área del rectángulo es", area)
