x=input("Historial de préstamos negativo o positivo: ")
y=input("Dispones de un empleo estable (tiene un empleo de más de 2 años de duración): ")
z=int(input("Sueldo: "))
b=z*0.1
a=int(input("Cántidad de préstamo solicitado: "))
if x=="positivo" and y=="estable" and b>=a:
    print("Préstamo aceptado")
elif x=="negativo" or y=="inestable" or b<a:
    print("Préstamo denegado")
else:
    print("Préstamo denegado")