lista=[]
n=1
perpe=False
while not perpe:
    if n<16:
      num1=int(input("Dime un número: "))
      lista.append(num1)
      n=n+1
    else:
       perpe=True
print(lista[::-1])