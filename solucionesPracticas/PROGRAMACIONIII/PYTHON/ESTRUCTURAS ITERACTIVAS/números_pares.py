"""Mostrar sólo los números pares desde 0 hasta el número ingresado (input).
Nota: para saber si un número es par hacer i % 2 == 0)"""

numero_maximo = int(input("Ingrese el número máximo: "))

for numero in range(0, numero_maximo + 1):
  if numero % 2 == 0:
    print(numero)


"""Explicación:

Se solicita al usuario que ingrese el número máximo (numero_maximo).
Se utiliza un bucle for para iterar desde el 0 hasta el numero_maximo (inclusive).
Dentro del bucle, se evalúa si el valor actual del contador (numero) es par utilizando el operador % (módulo).
Si el número es par, se imprime en la consola."""

