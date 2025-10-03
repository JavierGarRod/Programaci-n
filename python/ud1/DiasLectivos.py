dias=input("Dime un día de la semana: ")
match dias:
    case "lunes" | "martes" | "miércoles" | "jueves" |"viernes":
        print("Es un día lectivo")
    case "sábado" | "domingo":
        print("Es un día de descanso, en finde")
    case _:
        print("Error")
print("Error")