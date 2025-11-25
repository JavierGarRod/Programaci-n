def generaLista():
    notas=[]
    rep=True

    while rep:
        n = int(input("Introduce una nota. Introduce un número 0 o números <0 para terminar: "))
        if n <= 0:
            rep=False
        else:
            notas.append(n)

    return notas

def esValida(notas):
    if len(notas) == 0:
        print("No se introdujeron notas.")
    else:
        minimo = min(notas)
        maximo = max(notas)
        pos=0
        sin_repetido=True
        while sin_repetido and pos <len(notas):
            elemento = notas[pos+1]
            for i in range (pos,len(notas),1):
                if elemento!=i:
                    sin_repetido=True
                else:
                    sin_repetido=False
    if sin_repetido==True:
        print("La secuencia es VÁLIDA.")
    else:
        print("La secuencia NO es válida.")
    
    return (sin_repetido)

def calculaPuntos(notas):
    puntuacion=len(notas)

    return puntuacion

lista=generaLista()
valida=esValida(lista)
puntos=calculaPuntos(lista)

print(lista)
print(valida)
print(puntos)
