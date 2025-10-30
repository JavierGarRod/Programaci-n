cadena=[]
num=int(input("Dime un número: "))

while num > 0:
    digito = num % 10    
    cadena.append(digito)
    num = num // 10

cadena[::-1]
print(cadena)