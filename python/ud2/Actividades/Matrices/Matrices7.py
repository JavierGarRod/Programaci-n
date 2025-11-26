matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]]

def sumaColumnaPar(matriz):
    suma=0
    for fila in matriz:
        for i in range(len(fila)):
            if i%2==0:
                suma=suma+fila[i]
    
    return suma

columnaPar=sumaColumnaPar[matriz]
print(f"La suma de las columnas pares es: {columnaPar}")