nombres = []
puntuaciones = []
generos = []
while True:
    print("Selecciona una de las siguientes opciones (R, E, P, D, G, S)")
    print("R. Registrar juegos")
    print("E. Mostrar estadísticas")
    print("P. Juego con mayor puntuación")
    print("D. Detalle de un juego")
    print("G. Mostrar juegos de un género")
    print("S. Salir del programa")
    opcion = input("Introduce una opción: ").upper()
    if opcion == "R":
        print("Registrando juegos...")
        cantidad = int(input("¿Cuántos juegos deseas registrar?: "))
        for i in range(cantidad):
            print(f"Juego {i+1}:")
            nombre = input("Nombre del juego: ").upper()
            puntuacion = int(input("Puntuación (1-10): "))
            while puntuacion<=0 or puntuacion>=11:
                print("La puntuación debe estar entre 1 y 10.")
                puntuacion = int(input("Puntuación (1-10): "))        
            genero = input("Género del juego: ").upper()
            nombres.append(nombre)
            puntuaciones.append(puntuacion)
            generos.append(genero)
            print("Juegos registrados correctamente.")
    elif opcion == "E":
        print("Tu colección de juegos PSP:")
        if len(nombres) == 0:
            print("No hay juegos registrados todavía.")
        else:
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} | Puntuación: {puntuaciones[i]} | Género: {generos[i]}")
    elif opcion == "P":
        if len(nombres) == 0:
            print("No hay juegos registrados para evaluar.")
        else:
            max_puntuacion = max(puntuaciones)
            indice = puntuaciones.index(max_puntuacion)
            print(f"Mejor juego:{nombres[indice]} | Puntuación: {puntuaciones[indice]} | Género: {generos[indice]}")
    elif opcion == "D":
        if len(nombres) == 0:
            print("No hay juegos registrados.")
        else:
            buscar = input("Introduce el nombre del juego a buscar: ").upper()
            if buscar in nombres:
                i = nombres.index(buscar)
                print(f"{nombres[i]} | Puntuación: {puntuaciones[i]} | Género: {generos[i]}")
            else:
                print("Este juego no está en la lista del sistema.")
    elif opcion == "G":
        if len(nombres) == 0:
            print("\nNo hay juegos registrados.")
        else:
            genero_buscar = input("Introduce el género a filtrar: ").upper()
            encontrados = False
            print(f"Juegos del género '{genero_buscar}':")
            for i in range(len(nombres)):
                if generos[i].lower() == genero_buscar.lower():
                    print(f"- {nombres[i]} | Puntuación: {puntuaciones[i]} | Género: {generos[i]}")
                    encontrados = True
            if not encontrados:
                print("No hay juegos para ese género en la lista del sistema.")
    elif opcion == "S":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")