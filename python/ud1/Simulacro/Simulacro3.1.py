#Apartado A

def pedir_opcion(jugador):
    while True:
        opcion = input(f"{jugador}, elige 'pares' o 'nones': ").lower()
        if opcion in ["pares", "nones"]:
            return opcion
        print("Opción inválida. Escribe 'pares' o 'nones'.")

def pedir_dedos(jugador):
    while True:
        try:
            dedos = int(input(f"{jugador}, ¿cuántos dedos sacas (0 a 5)?: "))
            if 0 <= dedos <= 5:
                return dedos
            else:
                print("Debes elegir un número entre 0 y 5.")
        except ValueError:
            print("Debes ingresar un número entero entre 0 y 5.")

# Programa principal
print("Bienvenido al juego de Pares y Nones ")

jugador1 = pedir_opcion("Jugador 1")
# El jugador 2 tendrá la opción opuesta automáticamente
jugador2 = "pares" if jugador1 == "nones" else "nones"
print(f"Jugador 1 juega con {jugador1} y Jugador 2 con {jugador2}")

dedos1 = pedir_dedos("Jugador 1")
dedos2 = pedir_dedos("Jugador 2")

suma = dedos1 + dedos2
print(f"La suma de dedos es {suma}")

if suma % 2 == 0:
    ganador = "pares"
else:
    ganador = "nones"

if jugador1 == ganador:
    print("¡Gana el Jugador 1!")
else:
    print("¡Gana el Jugador 2!")