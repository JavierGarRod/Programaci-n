NumeroMes=int(input("Dime un número del 1 al 12: "))
match NumeroMes:
    case 1 | 2 | 3:
        if NumeroMes==1:
            print("Su mes es Enero")
        elif NumeroMes==2:
            print("Su mes es Febrero")
        else:
            print("Su mes es Marzo")
        print("Estás en Invierno")
    case 4 | 5 | 6:
        if NumeroMes==4:
            print("Su mes es Abril")
        elif NumeroMes==5:
            print("Su mes es Mayo")
        else:
            print("Su mes es Junio")
        print("Estás en Primavera")
    case 7|8|9:
        if NumeroMes==7:
            print("Su mes es Julio")
        elif NumeroMes==8:
            print("Su mes es Agosto")
        else:
            print("Su mes es Septiembre")
        print("Estás en Verano")
    case 10|11|12:
        if NumeroMes==10:
            print("Su mes es Octubre")
        elif NumeroMes==11:
            print("Su mes es Noviembre")
        else:
            print("Su mes es Diciembre")
        print("Estás en Otoño")
    case _:
        print("Error")
    

