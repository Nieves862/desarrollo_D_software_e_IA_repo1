num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segunda valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)


"""1-Se cargan por teclado tres números distintos.
Mostrar por pantalla el mayor de ellos."""

#==========================================================================

"""2-Se ingresa por teclado un valor entero, mostrar una leyenda que indique
si el número es positivo, negativo o nulo (es decir cero)"""

num=int(input("Ingrese un valor:"))
if num==0:
    print("Se ingresó el cero")
else:
    if num>0:
        print("Se ingresó un valor positivo")
    else:
        print("Se ingresó un valor negativo")

#==========================================================================

