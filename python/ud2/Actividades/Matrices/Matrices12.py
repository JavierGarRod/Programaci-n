def crear_matriz_suma(filas, columnas):
    matriz = []
    for i in range(1, filas + 1):
        fila = []
        for a in range(1, columnas + 1):
            fila.append(i + a)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Programa principal
matriz = crear_matriz_suma(4, 5)
mostrar_matriz(matriz)