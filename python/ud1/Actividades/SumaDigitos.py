numero=input("Introduce un número: ")
suma=0
for digito in numero:
    if digito.isdigit():
        suma+=int(digito)
print("La suma de los dígitos es: ",suma)
