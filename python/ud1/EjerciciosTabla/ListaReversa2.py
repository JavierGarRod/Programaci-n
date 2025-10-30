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
num2=int(input("Dime otro número: "))

if num2<len(lista):
   for i in range(0,num2):
      elemento=lista.pop()
      lista.insert(0,elemento)
else:
   print("El otro numero tiene que ser menor que los de la lista")
print(lista)