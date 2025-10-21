num1=0 or 1 or 2 or 3 or 4 or 5
import random
num2=random.randint(0,5)
apuesta2="P" or "I"
n=0 #numero de partidas jugadas
m=0 #numero de partidas perdidas
a=0 #numero de partidas ganadas
z=0 #apuesta humana mas frecuente (p)
y=0 #apuesta humana mas frecuente (i)
while num1!=num2:
    n=n+1
    num1=int(input("Dime un número de piedra (del 0 ma 5): "))
    num2=random.randint(0,5)
    while num1<0 or num1>5:
        num1=int(input("Dime un número del 0 al 5: "))
    apuesta1=input("¿Por que apuestas, par=p o impar=i?: ").upper()
    if apuesta1!="P":
        apuesta1="I"
        y=y+1
    elif apuesta1=="P":
        apuesta2=="I"
        z=z+1
    else:
        apuesta2=="P"
    suma=num1+num2
    print(suma)
    if suma%2==0 and apuesta1=="P":
        print("Has ganado")
    elif suma%2==0 and apuesta2=="P":
        print("Has perdido")
    elif suma%2!=0 and apuesta1=="I":
        print("Has ganado")
        a=a+1
    else:
        print("Has perdido")
        m=n-a
print("FIN, habeis introducido el mismo número de piedras")
print("Has jugado",n,"veces")
print("Has perdido",m,"veces")
print("Has ganado",a,"veces")
if z>y:
    print("La apuesta humana más frecuente ha sido la par con",z,"veces")
else:
    print("La apuesta humana más frecuente ha sido la impar con",y,"veces")