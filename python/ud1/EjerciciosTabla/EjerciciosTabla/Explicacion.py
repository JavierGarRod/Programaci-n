impares=[]
salir = False
numVeces = 0
while not salir: #Mientras que salir sea falso, repite todo lo siguiente
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce un segundo número: "))
    
    if num2 % num1 == 0: #Si num2 entre num1 iguala 0, salimos del while
        print("Saliendo del Programa")
        salir = True
    else: #Si num2 entre num1 es distinto que 0
        for i in range(num2,num1,-2): #Para i en el rango de num2 hasta num1 con salto de -2 en -2
            if i % 2 != 0: #Si i entre 2 es distinto que 0, imprime i y lo añade a la tabla
                print(i)
                impares.append(i)
    print("En total existen", len(impares), "números impares en el rango")
    print("=========================================")
    if numVeces>2: #Si numVeces es mayor que 2, sale del while
        salir=True
    else: #si numVeces en menor que 2 a numVeces se le suma 1
        numVeces+1
    impares=[] #Te vacia la tabla
print("FIN") #Al salir del while te imprime FIN