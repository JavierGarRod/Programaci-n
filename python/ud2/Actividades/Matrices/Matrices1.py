matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]]

# Devuelve el elemento dada la fila y columna
def obtener_elemento(fila, columna):
    return matriz[fila][columna]

# Devuelve la fila completa dado el número de fila
def obtener_fila(fila):
    return matriz[fila]

# Devuelve la columna completa dado el número de columna
def obtener_columna(columna):
    return [fila[columna] for fila in matriz]


print(obtener_elemento[1][2])  # Elemento en fila 1, columna 2 = 7
print(obtener_fila[0])         # Fila 0 = [8, 1, 6]
print(obtener_columna[1])      # Columna 1 = [1, 5, 9]