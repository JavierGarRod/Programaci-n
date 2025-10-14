n=int(input("Dime un número: "))
i= "*"
for i in range (n):
        if i%2==0:
            print("*" + "#"*(n-2) + "*")
        else:
            cadena=""
            for j in range(n):
                if j%2==0:
                        cadena=cadena+"*"
                else:
                        cadena=cadena+"@"
            print(cadena)