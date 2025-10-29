cadena=[]
cadena1=[]
capicua=False
n=0
while not capicua:
    num1=int(input("Dime un número: "))
    while num1 > 0:
        digito = num1 % 10    
        cadena.append(digito)
        num1 = num1 // 10
        n+1
    for i in reversed(cadena):
        cadena1.append(i)
    if cadena1==cadena:
        capicua=True
print("TRUE")