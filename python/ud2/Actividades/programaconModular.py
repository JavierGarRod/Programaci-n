num=input("Dime un número: ")
numInt=int(num)
salida=""

while len(num)<=4:
    num=input("Dime otro número")
    
if num%2==0:
    salida=num[2]+num[4]
elif num%3==0:
    salida=num[1]+num[2]
elif num%7==0:
    salida=num[0]+num[3]