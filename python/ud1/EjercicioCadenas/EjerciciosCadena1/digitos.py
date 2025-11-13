cadena=[]
n=0
num1=int(input("Dime un número: "))
num2=num1

while num1 > 0:
    digito = num1 % 10    
    cadena.append(digito)
    num1 = num1 // 10
    n +=1

print("El número",num2,"tiene",n,"dígitos")