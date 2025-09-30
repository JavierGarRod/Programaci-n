x=input("Tienes algun crédito vigente: ")
y=int(input("Ingreso anual: "))
if y>=60000 and x=="no":
    print("Préstamo aceptado")
elif y<60000 or x=="si":
    print("Préstamo denegado")
else:
    print("Préstamo denegado")