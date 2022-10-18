"""
8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto
dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en
el mes tomando en cuenta su sueldo base y comisiones.
Autor: Belén María León Fernández
Fecha:09/10/2022
"""
COMISION = 0.1
# Creamos la variable del sueldo base
sueldo_base = float(input("Introduce el sueldo base: "))

# Creamos las variables de ventas
venta1 = float(input("Precio de la venta1: "))
venta2 = float(input("Precio de la venta2: "))
venta3 = float(input("Precio de la venta3: "))

# Calculamos la comisión
comision_venta = COMISION * (venta1 + venta2 + venta3)

# Mostramos el resultado de la comisión
print("La comisión por venta es: ", comision_venta)

# Mostramos el sueldo total del vendedor
print("El sueldo total sera ", sueldo_base + comision_venta)
