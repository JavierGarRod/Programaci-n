num1=0 or 1 or 2 or 3 or 4 or 5
import random
num2=random.randint(0,5)
apuesta2="P" or "I"
while num1!=num2:
    num1=int(input("Dime un número de piedra (del 0 ma 5): "))
    num2=random.randint(0,5)
    while num1<0 or num1>5:
        num1=int(input("Dime un número del 0 al 5: "))
    apuesta1=input("¿Por que apuestas, par=p o impar=i?: ").upper()
    if apuesta1!="P":
        apuesta1="I"
    elif apuesta1=="P":
        apuesta2=="I"
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
    else:
        print("Has perdido")
print("FIN, habeis introducido el mismo número de piedras")