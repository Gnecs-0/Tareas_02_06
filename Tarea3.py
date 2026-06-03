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
    opc = int(input("Eliga una opción: "))
    if opc == 1:
        print("Su saldo es: ", saldo)
    elif opc == 2:
        depositar = int(input("Ingrese la cantidad a depositar: "))
        if depositar <= 0:
            print("Error! Ingrese una cantidad válida.")
        else:
            saldo += depositar
            print("El nuevo saldo es: ", saldo)
    elif opc == 3:
        retirar = int(input("Cuánto dinero desea retirar? "))
        if retirar > saldo:
            print("Error! No hay suficiente saldo para realizar esta operación.")
        elif retirar <= 0:
            print("Error! Ingrese una cantidad válida.")
        else:
            saldo -= retirar
            print("El nuevo saldo es: ", saldo)
    elif opc == 4:
        print("Gracias por usar el cajero automático")
        break