rep=True
tablero=[]
import random
tamaño=0
numMinas=0

while rep:
    print("Pulse T para generar un nuevo tablero")
    print("Pulse J para jugar")
    print("Pulse E para salir del juego")
    option=input("Elige una opción: ").upper()
    if option=="T":
        print("Generando tablero...")
        while tamaño<=7:
            mina=random.randint(0,1)
            if mina==0:
                tablero.append("")
            else:
                tablero.append("X")
                numMinas=numMinas+1
            tamaño=tamaño+1
        print("¡Tablero Generado! Se ha encontrado",numMinas,"minas. Tablero:",tablero)
    elif option=="J":
        print("Jugando...")
    elif option=="E":
        print("Saliendo...")
        rep=False
    else:
        print("La opción introducida es incorrecta")