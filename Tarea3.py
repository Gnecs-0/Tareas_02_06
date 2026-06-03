#Crear un programa de cajero automático que permita al usuario realizar las siguientes operaciones:
#1. Consultar saldo
#2. depositar dinero
#3. girar dinero
#4. Salir
#Reglas:
#Si intenta girar mas del dinero disponible, el programa debe mostrar un mensaje de error.
#El menu debe repetirse hasta que el usuario decida salir.
#Utilizar try-execpt para controlar ingresos incorrectos.
import os, time
os.system("cls")
print("Bienvenido al cajero automático")
time.sleep(2)
saldo = 100000

while True:
    os.system("cls")
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
        os.system("cls")
        print("Su saldo es de: ", saldo)
        time.sleep(2)
    elif opc == 2:
        while True:
            os.system("cls")
            try:
                depositar = int(input("Ingrese la cantidad a depositar: "))
                if depositar <= 0:
                    print("Error! Ingrese una cantidad válida.")
                    time.sleep(2)
                else:
                    saldo += depositar
                    print("El nuevo saldo es: ", saldo)
                    break
            except:
                print("Error! debe ingresar un número entero positivo.")
                time.sleep(2)
    elif opc == 3:
        while True:
            os.system("cls")
            try:
                retirar = int(input("Cuánto dinero desea retirar?: "))
                if retirar > saldo:
                    print("Error! No tiene suficiente saldo para retirar esa cantidad.")
                    time.sleep(2)
                    continue
                elif retirar <= 0:
                    print("Error! Debe ingresar un número mayor a 0.")
                    time.sleep(2)
                else:
                    saldo -= retirar
                    print("El nuevo saldo es: ", saldo)
                    time.sleep(2)
                    break
            except:
                print("Error! debe ingresar un número entero positivo.")
                time.sleep(2)
    elif opc == 4:
        print("Gracias por usar el cajero automático")
        break