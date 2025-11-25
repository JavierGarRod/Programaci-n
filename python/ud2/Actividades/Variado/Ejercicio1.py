def obtieneYValidaDatosDeEntrada():
    while True:
        try:
            numero = float(input("Introduce un número positivo: "))
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

numero_valido = obtieneYValidaDatosDeEntrada()
print(f"El número positivo introducido es: {numero_valido}")