
"""Piedra, papel y tijera en Python
Descripción:

Crearás un juego clásico de piedra, papel y tijera en Python.
El juego enfrentará al usuario contra la computadora,
donde cada uno elegirá una de las tres opciones ("piedra", "papel" o "tijera")
y la computadora determinará el ganador según las reglas del juego.

Estructura:
Importar librerías: Importarás la librería random para generar la elección aleatoria de la computadora.

Definir funciones:

- elegir_opcion_usuario(): Esta función solicitará al usuario que ingrese su elección
("piedra", "papel" o "tijera") y la validará.

- elegir_opcion_computadora():
Esta función generará aleatoriamente la elección de la computadora ("piedra", "papel" o "tijera").
determinar_ganador(opcion_usuario, opcion_computadora): Esta función comparará las opciones del
usuario y la computadora y determinará al ganador según las reglas del juego.

- mostrar_mensaje(resultado): Esta función mostrará un mensaje al usuario indicando el resultado del juego
(ganó, perdió o empató).

Código principal:

- Presentará un menú al usuario con las opciones disponibles ("piedra", "papel", "tijera" o "salir").
- Obtendrá la elección del usuario utilizando la función elegir_opcion_usuario().
- Generará la elección de la computadora utilizando la función elegir_opcion_computadora().
- Determinará al ganador utilizando la función determinar_ganador().
- Mostrará un mensaje al usuario indicando el resultado del juego utilizando la función mostrar_mensaje().
- Repetirá el proceso hasta que el usuario decida salir.
- Implementación:"""

import random

def elegir_opcion_usuario():
  # ...

def elegir_opcion_computadora():
  # ...

def determinar_ganador(opcion_usuario, opcion_computadora):
  # ...

def mostrar_mensaje(resultado):
  # ...

# Código principal
while True:
  opcion_usuario = elegir_opcion_usuario()
  if opcion_usuario == "salir":
    break

  opcion_computadora = elegir_opcion_computadora()

  resultado = determinar_ganador(opcion_usuario, opcion_computadora)
  mostrar_mensaje(resultado)

"""Explicación:

La función elegir_opcion_usuario()
utiliza un ciclo while para seguir pidiendo al usuario que ingrese una opción válida hasta que lo haga.

La función elegir_opcion_computadora()
utiliza la función randint() de la librería random
para generar un número aleatorio entre 1 y 3, y luego lo asigna a una de las opciones ("piedra", "papel" o "tijera").

La función determinar_ganador() compara las opciones del usuario y la computadora y
devuelve un mensaje indicando quién ganó, quién perdió o si hubo un empate.

La función mostrar_mensaje() imprime un mensaje al usuario indicando el resultado del juego.

Recursos adicionales:

Puedes agregar más funcionalidades al juego,
como permitir al usuario jugar contra otro jugador humano,
llevar un registro de las partidas jugadas o mostrar estadísticas.

También puedes utilizar técnicas de programación orientada a
objetos para crear una clase Juego que encapsule la lógica del juego.
"""
