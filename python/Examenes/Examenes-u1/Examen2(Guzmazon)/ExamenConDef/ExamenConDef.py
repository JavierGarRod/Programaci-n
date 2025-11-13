def cargaCesta(dineroMax):
    producto=[]
    precios=[]
    costeTotal=0
    rep=True
    total=0

    while rep:
        cesta=input("Intruduce el producto: ").upper()
        producto.append(cesta)
        coste=input("Intruduce el coste de su producto: ")
        precios.append(coste)
        total=total+float(coste)
        if float(total)>dineroMax:
                total=total-float(coste)
                lim=precios.index(coste)
                producto.pop(lim)
                precios.pop(lim)
                rep=False

    print("Importe máxigo a gastar:",dineroMax)
    print("Productos:",producto)
    print("Precios:",precios)
    print("Coste total de la cesta:",total)
    return producto, precios, costeTotal

def pinteMenu():
    print("Pulse S para calcular el dinero sobrante")
    print("Pulsa R para eliminar un producto y su precio")
    print("Pulsa C para devolver la lista de productos cuyo precio es más alto que un importe")

def leoOpcion(option,dineroMax,total,sobrante):
    option=input("Introduce una opción: ").upper()
    if option=="S":
        print("Sobrante")
        sobrante=dineroMax-total
    elif option=="R":
        print("Remove")
    elif option=="C": 
        print("Productos caros")
    else:
        print("Opción no válida")
    
    return option

importeAGastar=float(input("Intruduce el importe máx para gastarte: "))
resultados=cargaCesta(importeAGastar)
productos=resultados[0]
precios=resultados[1]
costeTotal=resultados[2]

print(pinteMenu)
opciones=leoOpcion()