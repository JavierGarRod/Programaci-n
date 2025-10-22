import random
humano=int(input("Piedra=0, papel=1 o tijera=2: "))
maquina=random.randint(0,2)
match humano:
    case 0 | 1 | 2:
        if humano==0 and maquina==2:
            print("Humano: piedra")
            print("Máquina: tijera")
            print("Has ganado")
        elif humano==0 and maquina==0 or maquina==1:
            print("Humano: piedra")
            if maquina==0:
                print("Máquina: piedra")
                print("Empate")
            else:
                print("Máquina: papel")
            print("Has perdido")
        elif humano==1 and maquina==0:
            print("Humano: papel")
            print("Máquina: piedra")
            print("Has ganado")
        elif humano==1 and maquina==1 or maquina==2:
            print("Humano: papel")
            if maquina==1:
                print("Máquina: papel")
                print("Empate")
            else:
                print("Máquina: tijera")
                print("Has perdido")
        elif humano==2 and maquina==1:
            print("Humano: tijera")
            print("Máquina: papel")
            print("Has ganado")
        elif humano==2 and maquina==2 or maquina==0:
            print("Humano: tijera")
            if maquina==1:
                print("Máquina: tijera")
                print("Empate")
            else:
                print("Máquina: piedra")
                print("Has perdido")
        else:
            print("Error")
    case _:
        print("Error") 