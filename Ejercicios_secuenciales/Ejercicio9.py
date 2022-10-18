"""
9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuanto deberá pagar finalmente por su compra.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
DESCUENTO = 0.15
# Pedimos que nos del precio
compra_sin_descuento = float(input("Dime el coste de la compra: "))

# Calculamos el precio
compra_con_descuento = compra_sin_descuento - (compra_sin_descuento * DESCUENTO)

# Mostramos el precio final
print("Precio final de la compra con el descuento es:", compra_con_descuento)
