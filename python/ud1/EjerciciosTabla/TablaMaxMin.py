lista=[]
for i in range(0,10):
    num=int(input("dime un número"))
    lista.append(num)

mayor=lista[0]
menor=lista[0]

for n in lista:
    if n > mayor:
        mayor=n
    elif n< menor:
        menor=n

print("La lista es:",lista)
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
