opcion=input("Dame una opción entre a, b o c: ")
match opcion:
    case "a":
       print("Alta")
    case "b":
        print("Baja")
    case "C":
        print("Cambio")
    case _:
        print("Inválido")
print("Error")

