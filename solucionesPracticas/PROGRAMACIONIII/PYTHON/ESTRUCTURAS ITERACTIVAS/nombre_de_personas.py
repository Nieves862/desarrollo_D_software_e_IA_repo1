"""Pedir que el usuario ingrese (input) nombre de personas y
mostrarlos hasta que el valor de lo que ingresa sea “fin” """

nombre = input("Ingrese un nombre (o 'fin' para terminar): ")

while nombre != "fin":
  print(nombre)
  nombre = input("Ingrese otro nombre (o 'fin' para terminar): ")
  
"""Explicación:

Se solicita al usuario que ingrese un nombre (nombre).
Se utiliza un bucle while para que se repita la solicitud de nombres mientras el valor ingresado no sea "fin".
Dentro del bucle, se imprime el nombre ingresado en la consola.
Se vuelve a solicitar un nombre al usuario."""

