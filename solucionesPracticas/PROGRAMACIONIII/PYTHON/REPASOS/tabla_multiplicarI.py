def tabla_multiplicar_while(numero):
    contador = 1
    while contador <= 10:
        resultado = numero * contador
        salida = f"{numero}x{contador}={resultado}"
        print(salida)
        contador += 1

if __name__ == "__main__":
    numero = int(input("Ingrese un número entre 1 y 10: "))
    if 1 <= numero <= 10:
        tabla_multiplicar_while(numero)
    else:
        print("El número debe estar entre 1 y 10.")
