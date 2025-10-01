NumeroMes=int(input("Dime un número entre el 3, 6, 9 y 12: "))
match NumeroMes:
    case 3 | 6:
        if NumeroMes==3:
            print("Su mes es Marzo")
            dia=int(input("Dime el día: "))
            if dia<=20 and dia>0:
                print("Es invierno")
            elif dia>20 and dia<30:
                print("Es primavera")
            else:
                print("Error")
        else:
            print("Su mes es Junio")
            dia=int(input("Dime el día: "))
            if dia>20 and dia<30:
                print("Es primavera")
            elif dia>20 and dia<30:
                print("Es verano")
            else:
                print("Error")
        
    case 9 | 12:
        if NumeroMes==9:
            print("Su mes es Septiembre")
            dia=int(input("Dime el día: "))
            if dia<=20 and dia>0:
                print("Es verano")
            elif dia>20 and dia<30:
                print("Es otoño")
            else:
                print("Error")
        else:
            print("Su mes es Diciembre")
            dia=int(input("Dime el día: "))
            if dia<=20 and dia>0:
                print("Es otoño")
            elif dia>20 and dia<30:
                print("Es invierno")
            else:
                print("Error")
    case _:
        print("Error")