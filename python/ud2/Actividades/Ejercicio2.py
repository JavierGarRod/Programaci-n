def esMultiplo(a, b):
    return a % b == 0

rep=True

while rep:
    # Pedimos los dos números al usuario
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))

    # Comprobamos si alguno es múltiplo del otro
    if esMultiplo(num1, num2):
        print(f"{num1} es múltiplo de {num2}.")
    elif esMultiplo(num2, num1):
        print(f"{num2} es múltiplo de {num1}.")
    else:
        print("Ninguno de los dos números es múltiplo del otro.")