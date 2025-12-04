def mostrarMenu():
    rep=True
    while rep:
        print("A) Registrar puntuaciones de equipo")
        print("L) Listar equipos y su puntuación por fase")
        print("C) Clasificados por fase")
        print("S) Salir")
        opcion=input("Introduce una opción: ").upper()
        if opcion=="A" or "L" or "C" or "S":
            rep=False
    
    return opcion

def registroPuntuacion(opcion):
    if opcion=="A":
        fase=int(input("En que fase se encuentra (1,2 o 3): "))
        nombre=[]
        puntuaciones=[]
        if fase ==1:
            rep1=0
            while rep1<8:
                nombreEquipo=input("Introduce el nombre del equipo: ")
                puntuacion=int(input("Introduce su puntuación: "))
                nombre.append(nombreEquipo)
                puntuaciones.append(puntuacion)
                rep1=rep1+1
        elif fase ==2:
            rep1=0
            while rep1<4:
                nombreEquipo=input("Introduce el nombre del equipo: ")
                puntuacion=int(input("Introduce su puntuación: "))
                nombre.append(nombreEquipo)
                puntuaciones.append(puntuacion)
                rep1=rep1+1
        elif fase ==3:
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

menu=mostrarMenu()
print(menu)
#registro=registroPuntuacion(opcion)
#print(registro)
        