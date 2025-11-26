matriz = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

def devuelveDiagonal(matriz):
    linea = 0
    posi = 0
    lista = []
    for i in range(len(matriz)):
        lista.append(matriz[linea][posi])
        linea += 1
        posi += 1
    return lista

def otraDiagonal(matriz):
    linea = 0
    posi = len(matriz) - 1
    lista = []
    for i in range(len(matriz)):
        lista.append(matriz[linea][posi])
        linea += 1
        posi -= 1
    return lista

diagonal1=devuelveDiagonal(matriz)
diagonal2=otraDiagonal(matriz)

if len(matriz)==len(matriz(0)):
    print(diagonal1 and diagonal2)
else:
    print("La matriz no es cuadrada")