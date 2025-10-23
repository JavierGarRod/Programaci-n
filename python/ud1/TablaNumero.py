import random
lista1=[]
lista2=[]
lista3=[]
for i in range (20):
    num=random.randint(0,100)
    lista1.append(num)
for num in lista1:
    lista2.append(num**2)
    lista3.append(num**3)
print("Num/cuadr./cubo*")
for i in range(20):
    print(lista1[i],lista2 [i],lista3[i])