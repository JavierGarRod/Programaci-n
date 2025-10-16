num1=int(input("Dime un número: "))
num2=int(input("Dime otro número: "))
while num1==0 and num2==0:
    print("Error")
for i in range(num1,num2+1):
    print(i)
    i=num2-1