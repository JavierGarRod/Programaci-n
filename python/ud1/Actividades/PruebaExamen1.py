nom=input("Dime un nombre: ")
while nom!="exit":
    num=int(input("Dime tu nota: "))
    while num>100 or num<0:
        num=int(input("Dime tu nota: "))
    if num<=49 and num>=0:
        print("Suspenso")
    elif num<=59 and num>=50:
        print("Suficiente")
    elif num<=69 and num>=60:
        print("Bien")
    elif num<=89 and num>=70:
        print("Notable")
    elif num<=100 and num>=90:
        print("Sobresaliente")
    nom=input("Dime un nombre: ")
print("Saliendo...")