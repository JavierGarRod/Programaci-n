#Apartado B

import random

def pedir_opcion():
    while True:
        opcion = input("Elige 'pares' o 'nones': ").lower()
        if opcion in ["pares", "nones"]:
            return opcion
        print("Opción inválida. Escribe 'pares' o 'nones'.")

def pedir_dedos():
    while True:
        try:
            dedos = int(input("¿Cuántos dedos sacas (0 a 5)?: "))
            if 0 <= dedos <= 5:
                return dedos
            print("Número inválido. Debe ser entre 0 y 5.")
        except ValueError:
            print("Debes ingresar un número entero.")

# Programa principal
print("Bienvenido al juego de Pares y Nones")
jugador = pedir_opcion()
maquina = "pares" if jugador == "nones" else "nones"

print(f"Tú juegas con {jugador} y la máquina con {maquina}")

ganadas_jugador = 0
ganadas_maquina = 0

while True:
    dedos_jugador = pedir_dedos()
    dedos_maquina = random.randint(0, 5)
    print(f"La máquina saca {dedos_maquina} dedos.")

    if dedos_jugador == 0 and dedos_maquina == 0:
        print("Ambos sacaron 0 dedos. Fin del juego.")
        break

    suma = dedos_jugador + dedos_maquina
    print(f"La suma es {suma}")

    if suma % 2 == 0:
        ganador = "pares"
    else:
        ganador = "nones"

    if jugador == ganador:
        print("¡Ganas esta ronda!")
        ganadas_jugador += 1
    else:
        print("La máquina gana esta ronda.")
        ganadas_maquina += 1

print(f"Resultado final:")
print(f"Tú ganaste {ganadas_jugador} partidas.")
print(f"La máquina ganó {ganadas_maquina} partidas.")
print("¡Gracias por jugar!")