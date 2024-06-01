"""En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso.
Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo
(promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos
estudiantes del curso han rendido el examen."""

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

promedio = 0

for _ in range(cantidad_alumnos):
  nota = float(input("Ingrese la nota del alumno: "))
  promedio += nota

promedio /= cantidad_alumnos

if promedio > 8:
  print("Rendimiento elevado")
elif promedio >= 6:
  print("Rendimiento aceptable")
else:
  print("Rendimiento bajo")

"""Explicación:

Se solicita al usuario que ingrese la cantidad de alumnos (cantidad_alumnos).
Se inicializa una variable promedio en 0.
Se utiliza un bucle for para iterar la cantidad de veces indicada por cantidad_alumnos.
Dentro del bucle, se solicita al usuario que ingrese la nota de un alumno (nota) y se convierte a float.
Se acumula la nota en la variable promedio.
Al final del bucle, se calcula el promedio dividiendo promedio por cantidad_alumnos.
Se utiliza una estructura condicional if - elif - else para evaluar el rendimiento:
Si el promedio es mayor a 8, se imprime "Rendimiento elevado".
Si el promedio está entre 6 y 8, se imprime "Rendimiento aceptable".
En caso contrario, se imprime "Rendimiento bajo"."""

