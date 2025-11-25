def segundo_a_hms(segundos):

    horas=segundos//3600
    min=segundos//60
    segundos=segundos

    return horas,"horas",min,"minutos",segundos,"segundos"

tiempo=True

while tiempo:
    print("S: Convertir a segundos")
    print("M: Convertir a minutos")
    print("H: Convertir a horas")
    print("-1: Salir del programa")
    opcion = input("Introduzca su elección: ") .upper()
    if opcion !="-1":
        entrada = input("Introduce el tiempo total en segundos (ej. 7385): ")
        segundos = int(entrada)

        if opcion == "H":
                resultado = segundo_a_hms(segundos)
                print("Desglose: ", str(resultado))

        elif opcion == "M":
                minutos = segundos / 60
                print(" Minutos: ", str(minutos))

        elif opcion == "S":
                print("Ya está en segundos: ", str(segundos))
    else:
        print("Saliendo del programa")
        tiempo=False
print("FIN")