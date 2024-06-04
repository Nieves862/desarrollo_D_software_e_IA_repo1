"""Actividad Parte I:

Iniciando

- Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos
(variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:
- Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 
- Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
- Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
- En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos
(nombre, apellido, dni, email, fecha de nacimiento)
- Guardar en una tupla los primeros n números pares.
- El valor de n que lo ingrese el usuario (input).
- Luego mostrar los datos de la tupla.
Nota: para saber si el número i es par hacer i % 2 == 0 """

#Parte 1: Pedir nombres, guardarlos en una lista y mostrarlos

#Definir la lista: Crea una lista vacía para almacenar los nombres:

nombres = []

#Ciclo para pedir nombres: Utiliza un ciclo for para pedir 10 nombres al usuario:

for i in range(10):
  nombre = input("Ingrese un nombre: ")
  # Verificar si el nombre ya está en la lista
  if nombre not in nombres:
    nombres.append(nombre)
  else:
    print(f"El nombre '{nombre}' ya está en la lista. Ingrese otro nombre: ")

#Mostrar la lista: Imprime la lista de nombres:

print("Nombres Ingresados:")
for nombre in nombres:
  print(nombre)

#Parte 2: Eliminar elementos, ordenar y mostrar la lista
#Eliminar la tercera persona: Utiliza el índice para eliminar el tercer elemento:

del nombres[2]

#Eliminar la última persona: Elimina el último elemento con la función pop():

nombres.pop()

#Ordenar la lista: Ordena la lista alfabéticamente:

nombres.sort()

#Mostrar la lista ordenada: Imprime la lista ordenada:

print("Lista ordenada:")
for nombre in nombres:
  print(nombre)

#Parte 3: Guardar datos de una persona en un diccionario
#Crear el diccionario: Crea un diccionario vacío para almacenar los datos de una persona:

persona = {}

#Pedir datos al usuario: Pide al usuario cada dato de la persona:

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = input("Ingrese el DNI: ")
email = input("Ingrese el email: ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")

# Agregar los datos al diccionario
persona["nombre"] = nombre
persona["apellido"] = apellido
persona["dni"] = dni
persona["email"] = email
persona["fecha_nacimiento"] = fecha_nacimiento

#Mostrar los datos de la persona: Imprime los datos del diccionario:

print("Datos de la persona:")
for clave, valor in persona.items():
  print(f"{clave}: {valor}")

#Parte 4: Guardar datos de 4 personas en un diccionario
#Crear el diccionario familia: Crea un diccionario vacío llamado familia para almacenar los datos de las 4 personas:

familia = {}


#Ciclo para agregar personas: Utiliza un ciclo for para agregar 4 personas a la familia:

for i in range(4):
    
# Crear el diccionario para la persona actual
  persona = {}

# Pedir datos al usuario
  nombre = input("Ingrese el nombre: ")
  apellido = input("Ingrese el apellido: ")
  dni = input("Ingrese el DNI: ")
  email = input("Ingrese el email: ")
  fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")

# Agregar los datos al diccionario de la persona actual
  persona["nombre"] = nombre
  persona["apellido"] = apellido
  persona["dni"] = dni
  persona["email"] = email
  persona["fecha_nacimiento"] = fecha_nacimiento

# Agregar la persona al diccionario familia con una clave única
  clave = f"persona_{i + 1}"  # Clave única para cada persona
  familia[clave] = persona

#Mostrar datos de la familia: Recorre el diccionario familia y muestra los datos de cada persona:

print("Datos de la familia:")
for clave, persona in familia.items():
  print(f"\n**{clave}:**")
  for campo, valor in persona.items():
    print(f"{campo}: {valor}")

#Parte 5: Guardar números pares en una tupla y mostrarlos
#Pedir el valor de n: Pide al usuario el valor de n:

n = int(input("Ingrese el valor de n: "))

#Crear una tupla vacía: Crea una tupla vacía para almacenar los números pares:

numeros_pares =
