"""Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento
del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los
jubilados. La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos,
se suma los descuentos). Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

Para cada caso hacer:

● Una breve descripción de la situación comentada en la cabecera del archivo.py

● Solución implementada en python en el mismo archivo donde se detalla la descripción."""


"""Casos de uso de estructuras condicionales:
1. Condicional parcial (solo el if) con expresión lógica simple
Descripción:

En este caso, la estructura condicional if se utiliza para evaluar una única condición y ejecutar un bloque de código si esta se cumple. No se incluye la rama else para manejar el caso contrario.

Ejemplo:"""

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    
"""En este ejemplo, se verifica si la variable edad es mayor o igual a 18. Si se cumple la condición, se imprime el mensaje "Eres mayor de edad"."""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""2. Condicional completo (if - else) con expresión lógica simple
Descripción:

En este caso, la estructura condicional if - else se utiliza para evaluar una única condición y ejecutar un bloque de código si esta se cumple, y otro bloque de código en caso contrario."""

Ejemplo:

es_estudiante = True

if es_estudiante:
    descuento = 50
else:
    descuento = 0

precio_total = precio_producto - descuento

print(f"Precio total: {precio_total}")

"""En este ejemplo, se verifica si la variable es_estudiante es True. Si se cumple la condición, se aplica un descuento del 50%, en caso contrario, el descuento es del 0%. Finalmente, se calcula el precio total y se imprime."""

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
 """ 3- Condicional parcial (solo el if) con expresión lógica compuesta (and)
Descripción:

En este caso, la estructura condicional if se utiliza para evaluar una expresión lógica compuesta, formada por dos o más condiciones unidas mediante la conjunción lógica and. Si todas las condiciones se cumplen, se ejecuta
el bloque de código correspondiente."""

Ejemplo:

usuario = "admin"
contrasena = "123456"

if usuario == "admin" and contrasena == "123456":
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")

"""En este ejemplo, se verifica si la variable usuario es igual a "admin" y la variable contrasena es igual a "123456". Si ambas condiciones se cumplen, se imprime el mensaje "Acceso concedido", en caso contrario, se imprime
"Usuario o contraseña incorrectos"."""

"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""4. Condicional completo (if - else) con expresión lógica compuesta (or)
Descripción:

En este caso, la estructura condicional if - else se utiliza para evaluar una expresión lógica compuesta, formada por dos o más condiciones unidas mediante la disyunción lógica or. Si se cumple al menos una de las condiciones,
se ejecuta el bloque de código correspondiente. En caso contrario, se ejecuta el bloque else.

Ejemplo:

dia_semana = "Domingo"

if dia_semana == "Sabado" or dia_semana == "Domingo":
    print("Fin de semana")
else:
    print("Día de semana")

""" En este ejemplo, se verifica si la variable dia_semana es igual a "Sabado" o "Domingo". Si se cumple al menos una de las condiciones, se imprime el mensaje "Fin de semana", en caso contrario, se imprime "Día de semana."""
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""



