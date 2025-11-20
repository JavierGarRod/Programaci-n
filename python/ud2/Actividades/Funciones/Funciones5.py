def estaOrdenadaAscendemente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def estaOrdenada(lista, ascendente):
    # Ascendente
    if ascendente:
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True

    # Descendente
    else:
        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                return False
        return True
    
print(estaOrdenadaAscendemente([1, 2, 3]))       
print(estaOrdenadaAscendemente([3, 2, 1]))       

print(estaOrdenada([1, 2, 3]))             
print(estaOrdenada([3, 2, 1]))           
print(estaOrdenada([1, 3, 2]))           
print(estaOrdenada([1, 3, 2]))    