# Apartado A

rep=True
impares = []

while rep:
    primero = int(input("Introduce el primer número: "))
    segundo = int(input("Introduce el segundo número: "))

    # Salida si ambos números son 0
    if primero == 0 and segundo == 0:
        print("Fin del programa.")
        rep=False

    # Validar que el primero sea menor que el segundo
    if primero >= segundo:
        print("El primer número debe ser menor que el segundo. Inténtalo de nuevo.")

    print("================================================")

    # Lista de números impares
    impares = []
    for num in range(primero, segundo + 1):
        if num % 2 != 0:
            impares.append(num)

    # Mostrar impares
    print(f"Impares que existen entre [{primero} - {segundo}]: ", end="")
    for i in range(len(impares)):
        if i < len(impares) - 1:
            print(impares[i])
        else:
            print(impares[i])
    print()

    # Mostrar total
    print(f"En total existen {len(impares)} números impares en el rango.")
    print("================================================")