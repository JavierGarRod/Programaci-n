rep=True

while rep:
    print("Pulse T para generar un nuevo tablero")
    print("Pulse J para jugar")
    print("Pulse E para salir del juego")
    option=input("Elige una opción: ").upper()
    if option=="T":
        print("Generando tablero...")
    elif option=="J":
        print("Jugando...")
    elif option=="E":
        print("Saliendo...")
        rep=False
    else:
        print("La opción introducida es incorrecta")