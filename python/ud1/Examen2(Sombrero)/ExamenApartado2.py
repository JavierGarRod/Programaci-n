print("==============================")
print("SOMBRERO SELECCIONADOR")
print("==============================")
print("1.Selecciona casa para un alumno")
print("2.Mostrar estadísticas")
print("Elige una opción. Si quieres salir del programa, escribe la opcón 1 y el nombre del personaje INNOMBRABLE")
opcion=input("Seleccione opción (1 o 2): ")
while opcion<"1" or opcion>"2":
    opcion=input("Seleccione opción: ")
if opcion=="1":
    print("Ejecutando y seleccionando casa...")
    numbre=input("Dime tu nombre: ")
    import random
    casa=random.randint(1,4)
    match casa:
        case 1:
            print("El sombrero dice que",numbre,"pertenece a GRYFFINDOR")
        case 2:
            print("El sombrero dice que",numbre,"pertenece a SLYTHERIN")
        case 3:
            print("El sombrero dice que",numbre,"pertenece a HUFFLEPUFF")
        case 4:
            print("El sombrero dice que",numbre,"pertenece a RAVENCLAW")
elif opcion=="2":
    print("Ejecutando y mostrando estadísticas...")
else:
    print("FIN")
