def suma_diagonal(matriz, esPrincipal=True):
    n = len(matriz)  # tamaño de la matriz (n x n)
    suma = 0
    
    if esPrincipal:
        # Diagonal principal: posiciones (0,0), (1,1), (2,2), ...
        for i in range(n):
            suma += matriz[i][i]
    else:
        # Diagonal secundaria: posiciones (0,n-1), (1,n-2), ...
        for i in range(n):
            suma += matriz[i][n - 1 - i]
    
    return suma

matriz = [
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
]

print("Suma diagonal principal:", suma_diagonal(matriz, True))
print("Suma diagonal secundaria:", suma_diagonal(matriz, False))