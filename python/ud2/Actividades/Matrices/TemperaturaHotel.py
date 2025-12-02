Matriz=[
    [22, 20, 19, 21],
    [18, 25, 23, 22],
    [19, 21, 20, 24],
    [17, 23, 22, 19],
    [24, 23, 27, 26]
    ]

def temMedia(listaNumero):
    media=0
    for numero in listaNumero:
        media=media+numero
    mediaTotal=media/len(listaNumero)

    return mediaTotal

def mediaFila(Matriz):
    fila=int(input("Dime que planta deseas saber la temperatura media (0 al 4): "))
    media2=0
    for numero in Matriz[fila]:
        media2=media2+numero
    mediaTotal2=media2/len(Matriz[fila])

    return mediaTotal2

#def mediaHotel(Matriz):
#    media3=0
#    for i in Matriz:  
#        media3=media3+i
#        mediaTotal3=media3/len(Matriz)
#
#    return mediaTotal3

def getColumna(Matriz,numColumna):
    columna=[]
    for numero in range(0,len(Matriz)):
        columna.append(Matriz[numero][numColumna])

    return columna

listaNumero=[22, 20, 19, 21]
mediaFila1=temMedia(listaNumero)
print(mediaFila1)

mediaPlanta=mediaFila(Matriz)
print(mediaPlanta)

#mediaHtel=mediaHotel(Matriz)
#print(mediaHtel)

Habitacion=getColumna(Matriz)
print(Habitacion)