#Ejercicio 2: Promedio de Notas

#Solicite la cantidad de notas.
#Ingrese cada nota utilizando un ciclo.
#Calcule el promedio.
#Indique si el estudiante aprueba o reprueba.
#Utilice try/except para controlar errores.
#Regla
#Aprueba con promedio mayor o igual a 4.0.

cant_notas = int(input("Ingrese la cantidad de notas: "))
for i in range(cant_notas):
    nota = float(input(f"ingrese la nota {i+1}: "))
