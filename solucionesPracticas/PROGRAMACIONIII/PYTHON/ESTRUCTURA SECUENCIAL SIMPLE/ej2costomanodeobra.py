"""Algoritmo para calcular el costo de mano de obra para pintar una pared (Estructura Simple en Python)
Descripción:

Este programa en Python ayuda a un pintor de casas a calcular el costo de mano de obra para pintar una pared rectangular de un galpón.

Pasos:

Solicitar las dimensiones de la pared:
Se solicitan al usuario los valores de la altura (altura) y el ancho (ancho) de la pared en metros.
Calcular la superficie:
Se calcula la superficie de la pared multiplicando la altura por el ancho y se almacena en la variable superficie.
Solicitar el costo por metro cuadrado:
Se solicita al usuario el costo que cobra el pintor por metro cuadrado de pintura.
Calcular el costo total de mano de obra:
Se multiplica la superficie de la pared por el costo por metro cuadrado y se almacena en la variable costo_mano_obra.
Mostrar el resultado:
Se imprime el valor de costo_mano_obra con un mensaje que indica el costo total de mano de obra para pintar la pared."""

#Código Python:

# Se inicializan las variables
altura = 0
ancho = 0
superficie = 0
costo_por_metro_cuadrado = 0
costo_mano_obra = 0

# Se solicitan las dimensiones de la pared
altura = float(input("Ingrese la altura de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))

# Se calcula la superficie
superficie = altura * ancho

# Se solicita el costo por metro cuadrado
costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado de pintura: "))

# Se calcula el costo total de mano de obra
costo_mano_obra = superficie * costo_por_metro_cuadrado

# Se muestra el resultado
print(f"El costo total de mano de obra para pintar la pared es de: ${costo_mano_obra:.2f}")

"""Explicación:

Entrada de datos:
Se utilizan las funciones input() y float() para solicitar al usuario los valores de la altura, el ancho y el costo por metro cuadrado.
Cálculos:
La superficie de la pared se calcula multiplicando la altura por el ancho y se almacena en superficie.
El costo total de mano de obra se calcula multiplicando la superficie por el costo por metro cuadrado y se almacena en costo_mano_obra.
Salida de datos:
Se imprime el valor de costo_mano_obra con un mensaje que indica el costo total de mano de obra. Se utiliza el formato .2f para mostrar
el costo con dos decimales.


Consideraciones:

Este código asume que la pared es rectangular y que el pintor cobra un precio único por metro cuadrado.
Puedes modificar el código para considerar diferentes formas de la pared o diferentes tipos de pintura que
podrían afectar el costo por metro cuadrado.
También puedes agregar validación de datos para asegurarte de que el usuario ingrese valores válidos para
la altura, el ancho y el costo por metro cuadrado."""
