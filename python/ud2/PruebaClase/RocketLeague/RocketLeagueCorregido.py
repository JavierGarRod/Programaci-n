# Diccionario global donde guardaremos las puntuaciones
puntuaciones = {
    "inicial": {},
    "semifinal": {},
    "final": {}
}

def pedir_fase():
    
    #Pide al usuario la fase y asegura que sea válida.
    #No recibe parámetros.
    #Devuelve la fase en minúsculas.
    
    while True:
        fase = input("Introduce la fase (inicial, semifinal, final): ").strip().lower()

        assert (fase=="inicial" or "semifinal" or "final")

        return fase


# ----------------------------
# MÉTODO REGISTRAR PUNTUACIONES
# ----------------------------
def registroPuntuaciones(fase):
    
    #Recibe la fase (str).
    #Pide por teclado los datos de cada equipo según la fase:
    #  - 8 en inicial
    #  - 4 en semifinal
    #  - 2 en final
    #Devuelve un diccionario con formato {equipo: puntos}
    nombre=[]
    puntuaciones=[]
    if fase =="inicial":
        rep1=0
        while rep1<8:
            nombreEquipo=input("Introduce el nombre del equipo: ")
            puntuacion=int(input("Introduce su puntuación: "))
            nombre.append(nombreEquipo)
            puntuaciones.append(puntuacion)
            rep1=rep1+1
    elif fase =="semifinal":
        rep1=0
        while rep1<4:
            nombreEquipo=input("Introduce el nombre del equipo: ")
            puntuacion=int(input("Introduce su puntuación: "))
            nombre.append(nombreEquipo)
            puntuaciones.append(puntuacion)
            rep1=rep1+1
    elif fase =="final":
        rep1=0
        while rep1<2:
            nombreEquipo=input("Introduce el nombre del equipo: ")
            puntuacion=int(input("Introduce su puntuación: "))
            nombre.append(nombreEquipo)
            puntuaciones.append(puntuacion)
            rep1=rep1+1
    else:
        print("Error")

    return nombre, puntuaciones


# ----------------------------
# MÉTODO LISTAR PUNTUACIONES
# ----------------------------
def listarPuntuacionesEquipo(fase, puntuaciones, nombre):
    #Recibe la fase y las puntuaciones registradas.
    #Imprime los equipos y puntuaciones si existen datos.
    
    fase1 = puntuaciones[fase]

    if len(fase1) == 0:
        print("===================================")
        print(f"La Fase {fase.upper()} no ha sido registrada en el sistema")
        print("===================================")
        return

    print("===================================")
    print(f"Fase {fase.upper()}")
    print("===================================")
    print(f"El equipo {nombre} ha obtenido {puntuaciones} puntos")


# ----------------------------
# MÉTODO CALCULAR CLASIFICADOS
# ----------------------------
def calculaClasificados(nombre, puntuaciones):
    max=0
    maxNom=""
    for i in range(len(puntuaciones)):
        if max < puntuaciones[i]:
            max=puntuaciones[i]
            maxNom=nombre[i]

    return max, maxNom

# ----------------------------
# PROGRAMA PRINCIPAL (MENÚ)
# ----------------------------
def mostrarMenu():
    rep=True

    while rep:

        print("========= MENÚ PRINCIPAL =========")
        print("R) Registrar puntuaciones de equipo")
        print("L) Listar equipos y su puntuación por fase")
        print("C) Clasificados por fase")
        print("S) Salir")
        print("=================================")

        opcion = input("Elige una opción: ").upper()

        if opcion == "R":
            fase = pedir_fase()
            puntuaciones[fase] = registroPuntuaciones(fase)

        elif opcion == "L":
            fase = pedir_fase()
            listarPuntuacionesEquipo(fase, puntuaciones)

        elif opcion == "C":
            fase = pedir_fase()
            calculaClasificados(fase, puntuaciones)

        elif opcion == "S":
            print("Saliendo del programa...")
            rep=False

        else:
            print("Opción incorrecta")
    
menu=mostrarMenu()
print(menu)