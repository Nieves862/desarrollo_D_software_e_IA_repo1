
"""Se ingresan tres valores por teclado que representan las notas de un alumno,
se obtiene el promedio sumando los tres valores y dividiendo por 3 dicho resultado
(Tener en cuenta que el resultado es un valor real ya que se utiliza el operador /).
Primeramente preguntamos si el promedio es superior o igual a 7,
en caso afirmativo va por la rama del verdadero
de la estructura condicional mostramos un mensaje que indica "Promocionado"
(con comillas indicamos un texto que debe imprimirse en pantalla).
En caso que la condición nos de falso, por la rama del
falso aparece otra estructura condicional, porque todavía debemos
averiguar si el promedio del alumno es superior o igual a cuatro o inferior a cuatro.
Estamos en presencia de dos estructuras condicionales compuestas."""


nota1=int(input("Ingrese primer Nota:"))
nota2=int(input("Ingrese segunda Nota:"))
nota3=int(input("Ingrese tercer Nota:"))
prom=(nota1+nota2+nota3)/3
if prom>=7:
    print("Aprobado")
else:
    if prom<=6:
        print("Regular")
    else:
        print("Reprobado")
