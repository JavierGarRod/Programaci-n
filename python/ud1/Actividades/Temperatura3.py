temperatura=float(input("Dime la temperatura de tu habitación"))
if temperatura<16:
    print("Enciende calefacción")
elif temperatura>26:
    print("Enciendo aire")
else:
    print("Sin acciones")
print("Registre la temperatura"+str(temperatura))