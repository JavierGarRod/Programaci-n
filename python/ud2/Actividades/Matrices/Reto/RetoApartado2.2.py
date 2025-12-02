ventas = [
    ["Portátil", 150, 799.99, 4.5],
    ["Smartphone", 250, 599.99, 4.3],
    ["Auriculares", 400, 49.99, 4.0],
    ["Tablet", 120, 299.99, 3.9],
    ["Monitor", 180, 199.99, 4.2],
    ["Smartwach", 220, 149.99, 4.1],
    ["Teclado mecánico", 300, 89.99, 4.4],
    ["Ratón gaming", 350, 59.99, 4.0],
    ["Cámara digital", 90, 999.99, 4.6],
    ["Consola", 200, 399.99, 4.7]
]

def getProducto(nombreProducto, ventas):
    encontrado=False
    i=0
    productos=[]

    while i<len(ventas) and not encontrado:
        if ventas[i][0]==nombreProducto:                            #Para recorrer la matriz
            encontrado=True
            productos=ventas[i]
            
        else:
            i=i+1
    
    return productos

def calculaIngresos(ventas, nombreProducto):
    ingresos=(getProducto(ventas,nombreProducto[1]))*(getProducto(ventas,nombreProducto[2]))

    return ingresos

def esProductoDestacado(ventas, nombreProducto):
    valoracion=getProducto(ventas,producto)
    destacado=False
    if len(valoracion)>0:
        if (getProducto(ventas,nombreProducto)[3])>=4.2:
            destacado=True
        else:
            destacado=False

    return destacado

def getProductoDestacado(ventas):
    lista=[]
    for elemento in ventas:
        if esProductoDestacado(ventas,elemento[0]):
            lista.append(elemento)
    
    return lista

nombreProducto=input("Dime el nombre del producto: ")
producto=getProducto(nombreProducto, ventas)
print(producto)
ingresosTotal=calculaIngresos(nombreProducto, ventas)
print(ingresosTotal)
productoDestacado=esProductoDestacado(ventas,nombreProducto)
print(productoDestacado)
listaDestacado=getProductoDestacado(ventas)
print(listaDestacado)