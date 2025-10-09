n=int(input("Dime un número: "))
i= "*"
for i in range(0, n-(n-1)):
        cadena1="*"+"#"*(n-2)+"*"
        print(cadena1)
        for j in range (0, n-2):
            cadena = "*"*(n)
            print(cadena)
        print(cadena1)