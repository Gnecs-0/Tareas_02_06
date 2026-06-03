#Ejercicio 2: Promedio de Notas

#Solicite la cantidad de notas.
#Ingrese cada nota utilizando un ciclo.
#Calcule el promedio.
#Indique si el estudiante aprueba o reprueba.
#Utilice try/except para controlar errores.
#Regla
#Aprueba con promedio mayor o igual a 4.0.
acumulador_notas = 0
cant_notas = int(input("Ingrese la cantidad de notas: "))
if cant_notas <= 0:
    print("La cantidad de notas debe ser mayor a cero.")


for i in range(cant_notas):
    nota = float(input(f"ingrese la nota {i+1}: "))
    if 1.0 <= nota <= 7.0:
        acumulador_notas += nota

promedio = acumulador_notas / cant_notas

if promedio >= 4.0:
    estado  = "Aprobado"
else:
    estado = "Reprobado"

print(f"El promedio de las notas es: {promedio}")
print(f"Estado: {estado}")