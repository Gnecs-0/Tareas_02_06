#Crear un programa de cajero automático que permita al usuario realizar las siguientes operaciones:
#1. Consultar saldo
#2. depositar dinero
#3. girar dinero
#4. Salir
#Reglas:
#Si intenta girar mas del dinero disponible, el programa debe mostrar un mensaje de error.
#El menu debe repetirse hasta que el usuario decida salir.
#Utilizar try-execpt para controlar ingresos incorrectos.
print("Bienvenido al cajero automático")
saldo = 100000

while True:
    print("""1. Consultar saldo
2. depositar dinero
3. Girar dinero
4. Salir""")
    while True:
        try:
            opc = int(input("Eliga una opción: "))
            if opc < 1 or opc > 4:
                print("Error! Debe ingresar un número entre 1 y 4.")
            else:
                break
        except:
            print("Error! debe ingresar un núemero entero positivo.")
    if opc == 1:
        print("Su saldo es de: ", saldo)
    elif opc == 2:
        while True:
            try:
                depositar = int(input("Ingrese la cantidad a depositar: "))
                if depositar <= 0:
                    print("Error! Ingrese una cantidad válida.")
                else:
                    saldo += depositar
                    print("El nuevo saldo es: ", saldo)
                    break
            except:
                print("Error! debe ingresar un número entero positivo.")
    elif opc == 3:
        while True:
            try:
                retirar = int(input("Cuánto dinero desea retirar?: "))
                print("Error! debe ingresar un número entero positivo.")
                if retirar > 0:
                    break
                elif retirar <= 0:
                    print("Error! Debe ingresar un número mayor a 0.")
                elif retirar > saldo:
                    print("Error! No tiene suficiente saldo para retirar esa cantidad.")
            except:
                print("Error! debe ingresar un número entero positivo.")
    elif opc == 4:
        print("Gracias por usar el cajero automático")
        break