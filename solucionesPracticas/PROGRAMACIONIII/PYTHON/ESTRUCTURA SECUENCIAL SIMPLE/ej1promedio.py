

"""Promedio de notas con Estructura Simple en Python
Descripción:

Este programa en Python ayuda a un estudiante a calcular el promedio de las notas de sus 5 materias.

Pasos:

Solicitar las notas:
Se utilizan las variables nota1, nota2, nota3, nota4, y nota5 para almacenar las notas de cada materia.
Se utiliza un ciclo for para solicitar al usuario que ingrese cada nota.
Calcular el promedio:
Se suma el valor de todas las notas utilizando la variable promedio.
Se divide el valor de promedio por la cantidad de materias (en este caso, 5).
Mostrar el promedio:
Se imprime el valor de promedio con un mensaje que indica que es el promedio general."""




# Se inicializan las variables
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
promedio = 0

# Se solicitan las notas al usuario
for i in range(1, 6):
  print(f"Ingrese la nota de la materia {i}:")
  nota = float(input())
  if nota >= 0 and nota <= 10:
    if i == 1:
      nota1 = nota
    elif i == 2:
      nota2 = nota
    elif i == 3:
      nota3 = nota
    elif i == 4:
      nota4 = nota
    else:
      nota5 = nota
  else:
    print("Error: La nota debe estar entre 0 y 10.")
    i -= 1  # Se repite la solicitud de la nota

# Se calcula el promedio
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Se muestra el promedio
print(f"El promedio general es: {promedio:.2f}")

"""
Explicación:

Ciclo for:
Se utiliza el ciclo for para repetir la solicitud de las notas 5 veces.
La variable i controla la iteración del ciclo, tomando valores desde 1 hasta 5.
Dentro del ciclo, se imprime un mensaje indicando qué nota se está solicitando.
Se utiliza la función float() para convertir la entrada del usuario (que se espera sea un string) a un número decimal.
Se verifica que la nota ingresada esté entre 0 y 10. Si no lo está, se muestra un mensaje de error y se repite la solicitud de la nota.
Se asigna la nota ingresada a la variable correspondiente (nota1, nota2, etc.) según el valor de i.
Cálculo del promedio:
Se suman todas las notas almacenadas en las variables nota1, nota2, etc. en la variable promedio.
Se divide el valor de promedio por 5, que es la cantidad de materias.
Mostrar el promedio:
Se imprime el valor de promedio con un mensaje que indica que es el promedio general. Se utiliza el formato .2f para mostrar el promedio con dos decimales.

La letra "f" en print(f"Ingrese la nota de la materia {i}:") indica que se está utilizando una cadena de formato formateada, también conocida como f-string.

¿Qué son las f-strings?

Las f-strings son una forma nueva e intuitiva de formatear cadenas en Python 3.6 y versiones posteriores. Permiten incluir expresiones Python directamente
dentro de las cadenas, lo que las hace más fáciles de leer y escribir que los métodos tradicionales de formato de cadenas como str.format() o el operador %.

¿Cómo funcionan las f-strings?

Las f-strings se identifican por la letra "f" o "F" antes de la cadena literal. Dentro de la cadena, se utilizan llaves {} para insertar expresiones Python. Estas expresiones pueden ser variables, cálculos matemáticos, llamadas a funciones, etc.

En el ejemplo que proporcionaste:

f"Ingrese la nota de la materia {i}:" es una f-string.
i es una expresión Python que contiene el valor actual del índice del ciclo for.
Las llaves {} alrededor de i indican que se debe insertar el valor de i en ese punto de la cadena"""
