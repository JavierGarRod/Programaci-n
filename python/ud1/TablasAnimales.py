lista=["elefante","perro","gato"]
animal=input("Dime un animal para ver si esta en la lista: ")
if animal in lista:
    print(animal, "se encuentra en la lista")
elif animal not in lista:
    print(animal, "no se encuentra en la lista")
else:
    print("Error")
print("FIN")