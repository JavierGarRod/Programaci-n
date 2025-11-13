print("==============================")
print("SOMBRERO SELECCIONADOR")
print("==============================")
print("1.Selecciona casa para un alumno")
print("2.Mostrar estadísticas")
print("Elige una opción. Si quieres salir del programa, escribe la opcón 1 y el nombre del personaje INNOMBRABLE")
opcion=input("Seleccione opción (1 o 2): ").upper()
num=0 #numero de alumnos
numG=0 #numero de alumnos en la casa G
numS=0 #numero de alumnos en la casa S
numH=0 #numero de alumnos en la casa H
numR=0 #numero de alumnos en la casa R
while opcion!="1 VOLDEMORT":
    while opcion<"1" or opcion>"2":
        opcion=input("Seleccione opción: ")
    if opcion=="1":
        print("Ejecutando y seleccionando casa...")
        numbre=input("Dime tu nombre: ").upper()
        import random
        casa=random.randint(1,4)
        match casa:
            case 1:
                print("El sombrero dice que",numbre,"pertenece a GRYFFINDOR")
                numG=numG+1
            case 2:
                print("El sombrero dice que",numbre,"pertenece a SLYTHERIN")
                numS=numS+1
            case 3:
                print("El sombrero dice que",numbre,"pertenece a HUFFLEPUFF")
                numH=numH+1
            case 4:
                print("El sombrero dice que",numbre,"pertenece a RAVENCLAW")
                numR=numR+1
    elif opcion=="2":
        print("Ejecutando y mostrando estadísticas...")
    else:
        print("ERROR")
    print("==============================")
    print("SOMBRERO SELECCIONADOR")
    print("==============================")
    print("1.Selecciona casa para un alumno")
    print("2.Mostrar estadísticas")
    print("Elige una opción. Si quieres salir del programa, escribe la opcón 1 y el nombre del personaje INNOMBRABLE")
    opcion=input("Seleccione opción (1 o 2): ").upper()
num=numG+numS+numH+numR
print("Apparition,transpórtame a otro sitio")
print("Alumnos total:",num)
print("Gryffindor:",numG)
print("Slytherin:",numS)
print("Hufflepuff:",numH)
print("Ravenclaw:",numR)