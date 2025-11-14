def obtengoLista():
    lista=[]
    rep=True
    while rep:
        num=int(input("Introduce un número, pulse -0 para salir: "))
        lista.append(num)
        if num==-0:
            rep=False

    return lista

def calculaListaInversa(lista):
    invertida=[]
    invertida=lista[::-1]

    return invertida

listaInicial=obtengoLista()
listaInversa=calculaListaInversa(listaInicial)
print(listaInversa)