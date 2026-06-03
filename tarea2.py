#Ejercicio 2: Promedio de Notas

#Solicite la cantidad de notas.
#Ingrese cada nota utilizando un ciclo.
#Calcule el promedio.
#Indique si el estudiante aprueba o reprueba.
#Utilice try/except para controlar errores.
#Regla
#Aprueba con promedio mayor o igual a 4.0.
import os, time
os.system("cls")
print("Bienvenido al promedio de Notas")
time.sleep(2)
acumulador_notas = 0
while True:
    os.system("cls")
    try:
        cant_notas = int(input("Ingrese la cantidad de notas: "))
        if cant_notas <= 0:
            print("La cantidad de notas debe ser mayor a cero.")
            time.sleep(2)
        else:
            break
    except:
        print("Error! Debe ingresar un número entero positivo.")
        time.sleep(2)        


for i in range(cant_notas):
    while True:
        os.system("cls")
        try:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if 1.0 <= nota <= 7.0:
                acumulador_notas += nota
                break
            else:
                print("Error! La nota debe estar entre 1.0 y 7.0.")
                time.sleep(2)
        except:
            print("Error! Debe ingresar un número positivo entre 1.0 y 7.0.")
            time.sleep(2)

promedio = acumulador_notas / cant_notas
if promedio >= 4.0:
    estado  = "Aprobado"
else:
    estado = "Reprobado"
#lo que se muestra al usuario
print(f"El promedio de las notas es: {promedio}")
print(f"Estado: {estado}")