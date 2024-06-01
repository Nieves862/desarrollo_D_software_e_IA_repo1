"""Estructuras Iterativas
Actividades
En estos apartados de Actividades se proponen ejercicios para que se realicen el  análisis
(detallando los datos de entrada poniendo nombre a las variables y tipo de dato,
el resultado o salida, indetificando nombre de variables y tipo de datos, y los calculos o proceso),
la implementación en python (archivos.py). Cada solución puede ser almacenada en un repositorio personal de github que luego puede compartir.

Consignas de Estructuras iterativas

Mostrar los números desde el 0 al número solicitado al usuario (input)"""

numero_maximo = int(input("Ingrese el número máximo: "))

for numero in range(0, numero_maximo + 1):
  print(numero)

"""Explicación:

Se solicita al usuario que ingrese el número máximo (numero_maximo).
Se utiliza un bucle for para iterar desde el 0 hasta el numero_maximo (inclusive).
Dentro del bucle, se imprime el valor actual del contador (numero) en cada iteración"""

