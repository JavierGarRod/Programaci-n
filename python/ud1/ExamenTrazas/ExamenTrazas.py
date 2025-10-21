print("Inicio")
x=int(input("Introduce un número: "))
contador=0
while x>0 and contador<3:
    if x % 2==0:
        for i in range (3,0,-1):
            x=x-1
    else:
        x=x-contador
        contador=contador+1
        print("X:",x,"Contador:",contador)
print("Resultado:",x)
print("FIN")