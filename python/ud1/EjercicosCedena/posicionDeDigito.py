num=int(input("Dime un número: "))
cadena=[]

while num > 0:
    digito = num % 10    
    cadena.append(digito)
    num = num // 10

num2=int(input("Dime un número haber si está: "))

if num2 in cadena:
    print(cadena.index(num2))
else:
    print("-1")
