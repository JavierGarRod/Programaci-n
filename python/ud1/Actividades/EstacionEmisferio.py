mes=int(input("Dime el mes de hoy: "))
dia=int(input("Dime el día de hoy: "))
hemis=input("En que hemisferio se encuentra: ").upper()
while (hemis !="SUR") and (hemis !="NORTE"):
    hemis=input("En que hemisferio se encuentra, sur o norte: ")
if hemis=="NORTE":
        match mes:
          case 3:
            if dia>=21:
              print("Estás en primavera")
          case 6:
            if dia>=21:
              print("Estás en verano")
          case 9:
            if dia>=23:
              print("Estás en otoño")
          case 12:
            if dia>=21:
              print("Estás en invierno")
          case 1|2:
            print("Estás en invierno")
          case 4|5:
            print("Estás en primavera")
          case 7|8:
            print("Estás en verano")
          case 10|11:
            print("Estás en otoño")
elif hemis=="SUR":
  match mes:
          case 3:
            if dia>=21:
              print("Estás en otoño")
          case 6:
            if dia>=21:
              print("Estás en invierno")
          case 9:
            if dia>=23:
              print("Estás en primavera")
          case 12:
            if dia>=21:
              print("Estás en verano")
          case 1|2:
            print("Estás en verano")
          case 4|5:
            print("Estás en otoño")
          case 7|8:
            print("Estás en invierno")
          case 10|11:
            print("Estás en primavera")
else:
  print("Error")