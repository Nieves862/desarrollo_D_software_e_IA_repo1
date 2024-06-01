"""Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10.
Por ejemplo para el 3 debería aparecer como salida:

3x1=3
3x2=6
3x3=9
…. y así hasta 10

Resuelva este problema utilizando un mientras y de modo que por la salida se emita la tabla tal como se propone.
Resuelva este problema utilizando un para y de modo que por la salida se emita la tabla tal como se propone."""

#Solución 1: Utilizando un bucle while

def tabla_multiplicar_while(numero):
  """
  Genera la tabla de multiplicar de un número usando un bucle `while`.

  Args:
    numero: El número para el que se quiere generar la tabla.
  """

  if not 1 <= numero <= 10:
    raise ValueError("El número debe estar entre 1 y 10")

  multiplicador = 1

  while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero}x{multiplicador}={resultado}")
    multiplicador += 1


numero = int(input("Ingrese un número (entre 1 y 10): "))
tabla_multiplicar_while(numero)

"""Explicación:

Se define una función tabla_multiplicar_while que recibe como parámetro el número para el que se quiere generar la tabla.
Se valida que el número esté entre 1 y 10, lanzando una excepción ValueError si no es así.
Se inicializa una variable multiplicador en 1.
Se utiliza un bucle while para iterar mientras multiplicador sea menor o igual a 10.
Dentro del bucle, se calcula el resultado de multiplicar numero por multiplicador (resultado).
Se imprime la tabla de multiplicar en el formato deseado.
Se aumenta el valor de multiplicador en 1.
Al final, se solicita al usuario que ingrese un número y se llama a la función tabla_multiplicar_while para generar la tabla correspondiente."""

#Solución 2: Utilizando un bucle for

def tabla_multiplicar_for(numero):
  """
  Genera la tabla de multiplicar de un número usando un bucle `for`.

  Args:
    numero: El número para el que se quiere generar la tabla.
  """

  if not 1 <= numero <= 10:
    raise ValueError("El número debe estar entre 1 y 10")

  for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero}x{multiplicador}={resultado}")


numero = int(input("Ingrese un número (entre 1 y 10): "))
tabla_multiplicar_for(numero)

"""Explicación:

Se define una función tabla_multiplicar_for que recibe como parámetro el número para el que se quiere generar la tabla.
Se valida que el número esté entre 1 y 10, lanzando una excepción ValueError si no es así.
Se utiliza un bucle for para iterar desde 1 hasta 10 (inclusive).
Dentro del bucle, se calcula el resultado de multiplicar numero por el valor actual del contador (multiplicador) (resultado).
Se imprime la tabla de multiplicar en el formato deseado.
Al final, se solicita al usuario que ingrese un número y se llama a la función tabla_multiplicar_for para generar la tabla correspondiente.
Ambas soluciones generan la tabla de multiplicar del número ingresado por el usuario de la misma manera, utilizando un bucle while en la primera
solución y un bucle for en la segunda. La elección entre una y otra depende del estilo de programación que se prefiera..."""





