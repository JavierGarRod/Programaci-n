x=int(input("Dime un número"))
y=int(input("Dime otro número"))
if x<0 and y<0:
    print("Sus números son negativos")
elif x==0 and y==0:
    print("Sus número son 0")
elif x>0 and y>0:
    print("Sus números son positivos")
else:
    print("Tienes un número negativo y otro positivo")