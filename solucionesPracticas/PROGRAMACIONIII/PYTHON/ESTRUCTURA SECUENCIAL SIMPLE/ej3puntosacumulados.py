
"""Algoritmo para calcular el puntaje total de un equipo de fútbol (Estructura Simple en Python)
Descripción:

Este programa en Python ayuda a un hincha de fútbol a calcular la cantidad de puntos que su equipo lleva acumulados en el campeonato,
en base a la cantidad de partidos ganados, empatados y perdidos."""

"""Pasos:

Solicitar la cantidad de partidos jugados:
Se solicita al usuario la cantidad total de partidos jugados (partidos_jugados) desde el inicio del campeonato.
Solicitar la cantidad de partidos ganados, empatados y perdidos:
Se solicitan al usuario la cantidad de partidos que el equipo ha ganado (partidos_ganados), empatado (partidos_empatados) y perdido
(partidos_perdidos).
Validar las cantidades ingresadas:
Se verifica que la suma de partidos_ganados, partidos_empatados y partidos_perdidos sea igual a partidos_jugados. Si no lo es, se
muestra un mensaje de error y se finaliza el programa.
Calcular el puntaje total:
Se calcula el puntaje total multiplicando la cantidad de partidos ganados por 3, la cantidad de partidos empatados por 1 y sumando los resultados.
Mostrar el resultado:
Se imprime el puntaje total con un mensaje que indica la cantidad de puntos que lleva el equipo acumulados en el campeonato.
Código Python:"""


# Se inicializan las variables
partidos_jugados = 0
partidos_ganados = 0
partidos_empatados = 0
partidos_perdidos = 0
puntaje_total = 0

# Se solicitan las cantidades
partidos_jugados = int(input("Ingrese la cantidad total de partidos jugados: "))
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

# Se valida la información
if partidos_jugados != (partidos_ganados + partidos_empatados + partidos_perdidos):
  print("Error: La suma de partidos ganados, empatados y perdidos no coincide con el total de partidos jugados.")
  exit()

# Se calcula el puntaje total
puntaje_total = (partidos_ganados * 3) + partidos_empatados

# Se muestra el resultado
print(f"El equipo lleva {puntaje_total} puntos acumulados en el campeonato.")


"""Explicación:

Entrada de datos:
Se utilizan las funciones input() y int() para solicitar al usuario la cantidad de partidos jugados, partidos ganados, partidos empatados y partidos perdidos.
Validación de datos:
Se verifica que la suma de partidos_ganados, partidos_empatados y partidos_perdidos sea igual a partidos_jugados. Si no lo es, se muestra un mensaje de error y se finaliza el programa. Esto es importante para garantizar que la información sea coherente.
Cálculo del puntaje:
Se calcula el puntaje total multiplicando la cantidad de partidos ganados por 3 (ya que cada partido ganado otorga 3 puntos), la cantidad de partidos empatados por 1 (ya que cada partido empatado otorga 1 punto) y sumando los resultados.
Salida de datos:
Se imprime el valor de puntaje_total con un mensaje que indica la cantidad de puntos que lleva el equipo acumulados en el campeonato.

Ejemplo de ejecución:
Ingrese la cantidad total de partidos jugados: 15
Ingrese la cantidad de partidos ganados: 8
Ingrese la cantidad de partidos empatados: 4
Ingrese la cantidad de partidos perdidos: 3
El equipo lleva 28 puntos acumulados en el campeonato.

Consideraciones:
Este código asume que el equipo solo ha jugado partidos ganados, empatados y perdidos.
No se consideran otros tipos de resultados como partidos suspendidos o postergados.
Puedes modificar el código para incluir estos otros tipos de resultados si es necesario.
También puedes agregar validación adicional para asegurarte de que el usuario ingrese valores
válidos para la cantidad de partidos jugados, ganados, empatados y perdidos."""
