def cargar_cadenas():
    #Pide cadenas al usuario hasta que introduzca una vacía.
    lista = []
    rep=True
    while rep:
        cadena = input("Introduce una cadena (Pulsa el enter para terminar): ")
        if cadena == "":
            rep=False
        lista.append(cadena)
    return lista


def eliminar_repetidas(lista):
    #Devuelve una lista sin cadenas repetidas, manteniendo el orden.
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def mostrar_lista(lista):
    #Imprime la lista
    print("Lista sin cadenas repetidas:")
    for elem in lista:
        print("-", elem)

lista = cargar_cadenas()
lista_sin_repetidas = eliminar_repetidas(lista)
mostrar_lista(lista_sin_repetidas)