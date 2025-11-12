dinero=float(input("Intruduce el dinero máximo que te quieres gastar en la compra: "))
producto=[]
precio=[]
rep=True
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