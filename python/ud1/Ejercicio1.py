num1=int(input("Dime un número: "))
num2=int(input("Dime un número: "))
num3=int(input("Dime un número: "))
while num1==0 and num2==0 and num3==0:
    print("Fin")
    num1=int(input("Dime un número: "))
    num2=int(input("Dime un número: "))
    num3=int(input("Dime un número: "))
if num2==num1+1 and num3==num2+1:
    print("Creciente")
elif num2==num1-1 and num3==num2-1:
    print("Decreciente")
else:
    print("Desordenado")
print("Fin")