numero=int(input("Dime un número: "))
if numero>0:
    for i in range(1,numero+1,1):
       print(i)
else:
    numero=int(input("Dime un número mayor que cero: "))
    for i in range(1,numero+1,1):
        print(i)
print("Error")

