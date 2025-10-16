año = int(input("Introduce un año (negativo para salir): "))

if año < 0:
        print("Programa terminado.")
elif (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("El año",año,"es bisiesto.")
else:
        print("El año",año,"no es bisiesto.")