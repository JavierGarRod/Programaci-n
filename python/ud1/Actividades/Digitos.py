num = int(input("Ingresa un número: "))
while num > 0:
    digito = num % 10
    print(digito)    
    num = num // 10