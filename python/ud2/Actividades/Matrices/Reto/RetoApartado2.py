matriz = [
    ['A', 'B', 'C', 'D'],    # Fila 1
    ['E', 'F', 'G', 'H'],    # Fila 2
    ['I', 'J', 'K', 'L'],    # Fila 3
    ['M', 'N', 'Ñ', 'O'],    # Fila 4
    ['P', 'Q', 'R', 'S'],    # Fila 5
    ['T', 'U', 'V', 'W'],    # Fila 6
    ['X', 'Y', 'Z', '_']     # Fila 7  (“_” representa el espacio)
]

cadena=("21,34,74,21,71,31,61,44,74,34,34,21,23,11,74,13,44,42,74,61,53,11,12,11,32,44,74,72,74,51,21,53,54,31,54,61,21,42,13,31,11")
cadena=cadena.split(",")

def descifrar(cadena, matriz):
    descifrado=[]
    for num in cadena:
        letras=matriz[int(num[0])-1][int(num[1])-1]
        descifrado.append(letras)

    return descifrado

cadena2=("NO SOLO HAY QUE CONFIAR EN EL PROCESO, HAY QUE SEGUIRLO")
cadena2=cadena2.split(" ")

def buscaLetraMatriz(letra,matriz):
    posicionFila=-1
    posicionColumna=-1
    for i in range(len(matriz)-1):
        fila=matriz(i)
        posicionColumna=buscaLetraEnLista(fila,letra)
        if posicionColumna!=-1: #Si es !=1--->en esa fila está la letra
            encontrado=True
            posicionFila=i
    
    return posicionFila+posicionColumna
    
def buscaLetraEnLista(listaLetra,letra):
    posicionColumna=-1
    # TODO #Devolverá la posición o -1 si no la encuentra

    return posicionColumna

def cifraMensaje(matriz,mensaje):
    mensajeCifrado=""
    for letra in mensaje:
        mensajeCifrado=mensajeCifrado+","+buscaLetraMatriz(matriz,letra)
    
    return mensajeCifrado


buscaLetraEnLista(matriz, cadena2)
descifrando=descifrar(cadena,matriz)
print(descifrando)