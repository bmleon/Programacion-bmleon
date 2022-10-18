"""
6. Calcular la media de tres números pedidos por teclado.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
num_pedidos = 3

# Creamos las variables
numero1 = float(input("Dime el primer número: "))
numero2 = float(input("Dime el segundo número: "))
numero3 = float(input("Dime el tercer número: "))

# Calculamos la media con los números pedidos por pantalla
media = (numero1 + numero2 + numero3) / num_pedidos

# Mostramos el resultado
print("La media de los números es: ", media)
