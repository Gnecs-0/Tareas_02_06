import os, time
os.system ("cls")

#estructura

nombre = input("Ingrese nombre del producto: ")
precio = int(input("Ingrese precio del producto: "))
descuento = int(input("Ingrese descuento: "))

#calculo

precio_desc = precio*((100-descuento)/100)

#Lo que se muestra}

print(f"""Producto: {nombre}
Precio original: {precio}
Descuento: {descuento}%
Precio final: {precio_desc}""")
