rep=True
while rep:
    print("A) Registrar puntuaciones de equipo")
    print("L) Listar equipos y su puntuación por fase")
    print("C) Clasificados por fase")
    print("S) Salir")
    opcion=input("Introduce una opción: ").upper
    if opcion=="S":
        print("Saliendo...")
        rep=False
    elif opcion=="A" or "L" or "C":
        rep=True
    else:
        print("Error")