mes=int(input("Dime el mes de hoy: "))
dia=int(input("Dime el día de hoy: "))
hemis=input("En que hemisferio se encuentra: ").upper()
while (hemis !="SUR") and (hemis !="NORTE"):
    hemis=input("En que hemisferio se encuentra, sur o norte: ")
if hemis=="NORTE":
    match mes:
            case 1|3:
              if dia
              print("Otoño")
            case 4|6:
              print("Invierno")
            case 7|9:
              print("Primavera")
            case 10|12:
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