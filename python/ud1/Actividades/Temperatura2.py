temperatura=int(input("Dime la temperatura de la habitación"))
if temperatura>26:
    print("Enciendo aire")
    temperatura=float(input("Dime ahora la temperatura de tu habitación"))
    if temperatura<23:
        print("Apago el aire")
else:
    print("No encender aire")
    if temperatura<10:
            print("Enciendo calefacción")
print("Registro la temperatura"+str(temperatura))