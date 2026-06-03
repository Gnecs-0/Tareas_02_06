import os, time
os.system ("cls")

#estructura
while True:
    os.system ("cls")
    nombre = input("Ingrese nombre del producto: ").strip()
    if nombre.isalpha():
        break
    else:
        print("Error: El nombre del producto debe contener solo letras. Intente nuevamente.")
        time.sleep(2)

while True:
    os.system ("cls")
    try:
        precio = int(input("Ingrese precio del producto: "))
        if precio > 0:
            break
        else:
            print("Error: El precio debe ser un número positivo. Intente nuevamente.")
            time.sleep(2)
    except:
        print("Error! Debe ingresar un número entero positivo para el precio.")
        time.sleep(2)

while True:
    os.system ("cls")
    try:
        descuento = int(input("Ingrese descuento: "))
        if 0 <= descuento <= 100:
            break
        else:
            print("Error: El descuento debe ser un número entre 0 y 100. Intente nuevamente.")
            time.sleep(2)
    except:
        print("Error! Debe ingresar un número entero positivo entre 0 y 100 para el descuento.")
        time.sleep(2)

#calculo

precio_desc = precio*((100-descuento)/100)

#Lo que se muestra

print(f"""Producto: {nombre}
Precio original: {precio}
Descuento: {descuento}%
Precio final: {precio_desc}""")
