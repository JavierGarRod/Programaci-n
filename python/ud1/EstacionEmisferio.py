mes=input("Dime el mes de hoy: ")
mes.upper()
dia=int(input("Dime el día de hoy: "))
hemis=input("En que hemisferio se encuentra: ")
hemis.upper()
while hemis !="SUR" or "NORTE":
    hemis=input("En que hemisferio se encuentra, sur o norte: ")
while mes>12 and dia>31:
    if hemis=="NORTE":
        match dia:
                case 23|9:
                  print("Otoño")
                case 21|12:
                  print("Invierno")
                case 21|3:
                  print("Primavera")
                case 21|6:
                  print("Verano")
    else:
        match dia:
                case 23|9:
                  print("Primavera")
                case 21|12:
                  print("Verano")
                case 21|3:
                  print("Otoño")
                case 21|6:
                  print("Invierno")