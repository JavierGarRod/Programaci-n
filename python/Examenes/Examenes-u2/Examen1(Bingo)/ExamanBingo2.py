carton_bingo=[[5,21,38,50,63],
              [12,17,44,47,74],
              [1,29,"--",55,69],
              [9,25,32,59,61],
              [14,19,41,52,66]]

def generaAleatorio(numSalidos):
    import random
    numSalidos = []
    rep=1
    while rep<=24:
        num=random.randint(1, 75)
        if num not in numSalidos:
            numSalidos.append(num)
            rep=rep+1
    
    return numSalidos

def  buscaNumeroEnLista(fila, numero):
    i = 0
    encontrado = False
    posicion = -1

    while i < len(fila) and not encontrado:
        if fila[i] == numero:
            encontrado = True
            posicion = i
        else:
            i += 1

    return posicion

#def compruebaSiHayLineaEnFila(numSalidos,numfila,carton_bingo):
#    fila = carton_bingo[numfila]
#    buscaNumeroEnLista(numSalidos, numero)
#    if fila in numSalidos:
#        encontrado=True
#    else:
#        encontrado=False

#    return encontrado

def jugarALaLinea(carton_bingo,numSalidos,numfila):
    generaAleatorio(numSalidos)
    #compruebaSiHayLineaEnFila(numSalidos,numfila,carton_bingo)

def lineaEncontrada(numSalidos,fila,posicion,lista,numero):
    print("Se ha conseguido LÍNEA en el cartón.")
    print(f"-Números que han salido antes de completar la fila: {len(numSalidos)}")
    print(f"-Fila acertante: la nº {buscaNumeroEnLista(lista,numero)}:{fila}")
    print(f"-Lista de nº que han salido:{generaAleatorio(numSalidos)}")

numSalidos=[]
fila=[]   
lista=[]
numero=0
posicion=0
juega=jugarALaLinea(carton_bingo,numSalidos,fila)
finJuego=lineaEncontrada(numSalidos,fila,posicion,lista,numero)