"""
3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
# Importamos la función math.sqrt
import math

print("Calcular la hipotenusa de un triangulo rectángulo")

# Creamos las variables del triángulo
cateto1 = float(input("Inserta el número del primer cateto: "))
cateto2 = float(input("Inserta el número del segundo cateto: "))

# La formula de la Hipotenusa es H**2 = c1**2 +c2**2
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Mostramos el resultado de la fórmula
print("El resultado de la calcular la hipotenusa es: ", hipotenusa)
