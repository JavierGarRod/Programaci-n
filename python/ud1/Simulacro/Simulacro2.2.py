# Apartado B

rep=True

while rep:
    primero = int(input("Introduce el primer número: "))
    segundo = int(input("Introduce el segundo número: "))

    if primero == 0 and segundo == 0:
        rep=False

    if primero >= segundo:
        print("El primer número debe ser menor que el segundo. Intenta de nuevo.")

    # Preguntamos si el rango es abierto o cerrado
    tipo = input("El rango es abierto o cerrado? (a/c): ")

    # Ajustamos los límites según abierto/cerrado
    inicio = primero
    fin = segundo
    if tipo.lower() == "a":
        inicio += 1
        fin -= 1

    impares = ""
    contador = 0

    for i in range(inicio, fin + 1):
        if i % 2 != 0:
            if contador == 0:
                impares += str(i)
            else:
                impares += ", " + str(i)
            contador += 1

    print("================================================")
    print(f"Impares que existen entre [{primero} - {segundo}]: {impares}")
    print(f"En total existen {contador} números impares en el rango.")
    print("================================================")