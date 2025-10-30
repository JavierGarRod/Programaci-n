cadena=[]
num1=int(input("Dime un número: "))
n=0

while num1 > 0:
    digito = num1 % 10    
    cadena.append(digito)
    num1 = num1 // 10
    n=n+1

num2=int(input("Dime un número del 0 al",n,": "))
print(cadena.index(num1))