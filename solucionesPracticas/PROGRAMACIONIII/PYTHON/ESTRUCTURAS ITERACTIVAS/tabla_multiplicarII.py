def tabla_multiplicar_for(numero):
    for contador in range(1, 11):
        resultado = numero * contador
        salida = f"{numero}x{contador}={resultado}"
        print(salida)

if __name__ == "__main__":
    numero = int(input("Ingrese un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        tabla_multiplicar_for(numero)
    else:
        print("El número debe estar entre 1 y 10.")
