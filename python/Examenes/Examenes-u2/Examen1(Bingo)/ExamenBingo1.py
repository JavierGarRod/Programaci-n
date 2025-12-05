def getListaSinRepetidos(numColumna):
    columna1=[]
    lista=[]
    rep=0
    import random
    match numColumna:
        case 0:
            n1 = 1
            n2 = 15
        case 1:
            n1 = 16
            n2 = 30
        case 2:
            n1 = 31
            n2 = 45
        case 3:
            n1 = 46
            n2 = 60
        case 4:
            n1 = 61
            n2 = 75
    while rep<5:
        num=random.randint(n1, n2)
        if num not in lista:
            lista.append(num)
            rep=rep+1
    columna1 =lista
    if numColumna==2:
        columna1.pop(2)
        columna1.insert(2,"--")
    
    return columna1

def getCarton():
    colum0= getListaSinRepetidos(0)
    print(colum0)
    colum1= getListaSinRepetidos(1)
    print(colum1)
    colum2= getListaSinRepetidos(2)
    print(colum2)
    colum3= getListaSinRepetidos(3)
    print(colum3)
    colum4= getListaSinRepetidos(4)
    print(colum4)

carton=getCarton()