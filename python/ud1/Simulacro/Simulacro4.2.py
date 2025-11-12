letras=[]
palabras=[]

stop=True

letra=input("Introduce una letra: ").lower()
letras.append(letra)

while stop:
    palabra=input("Introduce palabras, escribe stop si no deseas guardar más letras: ").lower()
    if palabra!="stop":
        palabras.append(palabra)
    else:
        stop=False

print("La letra introducida es: ", letra)
print("La lista de palabras es", palabras , "y el número de palabras introducidas es ", len(palabra) )

#Apartado B

palabras_inicio=[]
palabras_contiene=[]

print("Introduzca E si desea devolver la lista de palabras que comienzan por la letra." )
print("Introduzca C si desea devolver la lista de palabras que contienen  la letra.")
print("Introduzca S para terminar el programa.")
option=input("Introduzca una opción: ").lower()

while option!="s":
    if option=="e":
        for i in palabras:
            if i[0]==0:
                if len(i)>0:
                    palabras_inicio.append(i)
        print("Lista: ", palabras_inicio)
    elif option=="c":
        for i in palabras:
            if i in palabras:
                palabras_contiene.append(i)
        print("Lista: ", palabras_contiene)

    else:
        print("No es una opción válida")
    print("Introduzca E si desea devolver la lista de palabras que comienzan por la letra." )
    print("Introduzca C si desea devolver la lista de palabras que contienen  la letra.")
    print("Introduzca S para terminar el programa.")
    option=input("Introduzca una opción: ").lower()
print("Saliendo del programa...")
print("FIN")