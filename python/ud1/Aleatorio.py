import random
numero=random.randint(1,10)
numero2=int(input("Adivina el número del 1 al 10: "))
while numero2!=numero:
    numero2=int(input("Has perdido, dime orto número: "))
print("Has ganado, el número a adivinar era: ", numero)