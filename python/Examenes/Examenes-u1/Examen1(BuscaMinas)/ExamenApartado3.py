rep=True
rep1=True
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
        puntuacion=0
        while rep1:
            posicion=int(input("Introduce una posición (0-7): "))
            lectura=tablero[posicion]
            if lectura=="X":
                tablero.insert(posicion,"1")
                puntuacion=puntuacion+1
                numMinas=numMinas-1
                print("¡MINA! +1 punto. [Puntación:",puntuacion,"| Minas restantes:",numMinas,"]")
            elif lectura=="1":
                print("Ya habías encontrado esta mina")
            else:
                puntuacion=puntuacion-1
                print("Agua... -1 punto. [Puntuación:",puntuacion,"| Minas restantes:",numMinas,"]")
                tablero.insert(posicion,"1")
            if numMinas==0:
                rep1=False
        print("¡Has encontrado todas las minas! Tu puntuación final es:",puntuacion)
    elif option=="E":
        print("Saliendo...")
        rep=False
    else:
        print("La opción introducida es incorrecta")