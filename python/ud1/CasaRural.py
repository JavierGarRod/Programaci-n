print("==========================")
print("=Habitación=Camas=Planta==")
print("==========================")
print("=1.Azul    =2    =Primera=")
print("==========================")
print("=2.Roja    =1    =Primera=")
print("==========================")
print("=3.Verde   =3    =Segunda=")
print("==========================")
print("=4.Rosa    =2    =Segunda=")
print("==========================")
print("=5.Gris    =1    =Tercera=")
print("==========================")
NumeroHabitacion=int(input("Dime un numero de habitación: "))
match NumeroHabitacion:
    case 1:
        print("Habitación: azul")
        print("Camas: 2")
        print("Planta: primera")
    case 2:
        print("Habitación: roja")
        print("Camas: 1")
        print("Planta: primera")
    case 3:
        print("Habitación: verde")
        print("Camas: 3")
        print("Planta: segunda")
    case 4:
        print("Habitación: rosa")
        print("Camas: 2")
        print("Planta: segunda")
    case 5:
        print("Habitación: Gris")
        print("Camas: 1")
        print("Planta: tercera")
    case _:
        print("Error")