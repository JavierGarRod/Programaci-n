dinero=float(input("Intruduce el dinero máximo que te quieres gastar en la compra: "))
producto=[]
precio=[]
rep=True
rep1=True
total=0

while rep:
    cesta=input("Intruduce el producto: ").upper()
    producto.append(cesta)
    coste=input("Intruduce el coste de su producto: ")
    precio.append(coste)
    total=total+float(coste)
    if float(total)>dinero:
            total=total-float(coste)
            lim=precio.index(coste)
            producto.pop(lim)
            precio.pop(lim)
            rep=False

print("Importe máxigo a gastar:",dinero)
print("Productos:",producto)
print("Precios:",precio)
print("Coste total de la cesta:",total)

while rep1:
    print("Pulse S para calcular el dinero sobrante")
    print("Pulsa R para eliminar un producto y su precio")
    print("Pulsa C para devolver la lista de productos cuyo precio es más alto que un importe")
    option=input("Introduce una opción: ").upper()
    if option=="S":
        print("Sobrante")
    elif option=="R":
        print("Remove")
    elif option=="C": 
        print("Productos caros")
    else:
        print("Opción no válida")
        rep1=False