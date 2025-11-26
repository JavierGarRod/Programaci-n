matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]]

def numPares(matriz):
    suma=0
    for i in range(len(matriz)):
        if i%2==0:
            for elementoFila in matriz[i]:
                suma=suma+elementoFila
    
    return suma

sumaFilaPares=numPares(matriz)
print(f"La suma de todas las filas pares de la matriz es: {sumaFilaPares}")

