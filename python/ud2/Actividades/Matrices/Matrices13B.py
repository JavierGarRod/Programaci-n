matriz = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]
]

def son_iguales(lista_numeros):
    iguales  = True
    i = 0
    while i < (len(lista_numeros)-1) and iguales:
        if lista_numeros[i] != lista_numeros[i+1]:
            iguales = False
        else:
             i = i + 1
    return iguales

def suma_lista_numeros(lista_numeros):
        suma_fila = 0
        for n in lista_numeros:
            suma_fila = suma_fila + n
        return suma_fila

def sumaPorFilas(matriz):
    suma = 0
    lista = []
    for fila in matriz:
        suma = suma_lista_numeros(fila)  
        lista.append(suma)

    return lista

resultado = sumaPorFilas(matriz)
print(resultado) 



def suma_por_filas_igual(matriz):
    lista_suma = sumaPorFilas(matriz)
    sonIguales = son_iguales(lista_suma)
    return sonIguales

def getColumna(Matriz,numColumna):
    columna=[]
    for numero in range(0,len(Matriz)):
        columna.append(Matriz[numero][numColumna])

    return columna

def sumaPorColumnas(matriz):
    suma2=0
    lista2=[]
    for posColumna in range(len(matriz[0])):
        columna=getColumna(matriz,posColumna)
        suma2=suma_lista_numeros(columna)
        lista2.append(suma2)
    
    return son_iguales(lista2)

def sumaPorColumnasIgual(matriz):
    lista_suma2=sumaPorColumnas(matriz)
    sonIguales2=son_iguales(lista_suma2)

    return sonIguales2

resultado = suma_por_filas_igual(matriz)
print(resultado)
resultado2=sumaPorColumnasIgual(matriz)
print(resultado2)