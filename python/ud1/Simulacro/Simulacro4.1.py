palabra=[]

stop=True

letra=input("Introduce una letra: ").lower()
palabra.append(letra)

while stop:
    if letra=="stop":
        stop=False
    else:
        letra=input("ntroduce letras, escribe stop si no deseas guardar más letras: ").lower()
        palabra.append(letra)
        if letra=="stop":
            stop=False

print("La letra introducida es: ", letra)
print("La lista de letras es", palabra , "y el número de letras introducidas es ", len(palabra) )