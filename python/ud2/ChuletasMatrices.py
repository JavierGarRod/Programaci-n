#Una matríz es una cadena de cadenas, es decir:
matriz=[[0,2,4],     #posicion 0
        [1,3,5],     #posicion 1
        [6,8,10]]    #posicion 2
#matriz=[[],[],[]]
matriz[1] #lectura por posicion matriz[1]=[1,3,5]
matriz[1][1] #lectura por posicion en especifico, elemento de la cedena 1 en la posicion 1, matriz[1][1]=3

def suma_fila(matriz,num_fila):
    suma=0
    for i in matriz[num_fila]:  
        suma=suma+i                     #Suma de todos los elementos de la fila 1
    print(suma)

    return suma

print(suma_fila(matriz,1))

def suma_filas(matriz):
    sumas=0
    for i in matriz:  
        sumas=sumas+i                     #Suma de todos los elementos de las filas
    print(sumas)

    return sumas

print(suma_filas(matriz))