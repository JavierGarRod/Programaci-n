def cargar_lista():
    lista = []
    rep=True
    while rep:
        dato = input("Introduce un número (Pulsa enter si deseas terminar): ")
        if dato=="":
            rep=False
        else:
            lista.append(float(dato))
    return lista


def estaOrdenada(lista):
    ordenada=True
    i=0
    while i<len(lista)-1 and ordenada:
        if lista[i]>lista[i+1]:
            ordenada=False
        i=i+1
    return ordenada


# Programa principal
lista = cargar_lista()
print("Lista introducida:", lista)

if estaOrdenada(lista):
    print("La lista está ordenada ascendentemente.")
else:
    print("La lista NO está ordenada ascendentemente.")