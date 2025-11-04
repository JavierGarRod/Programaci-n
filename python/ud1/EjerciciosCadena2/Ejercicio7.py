txt=input("javier garcía rodríguez")
salida=txt.split()
palabrasalida=""
for palabra in salida:
    print(palabra[0].upper())
    print(palabra[1:])
    palabrasalida=palabrasalida+palabra[0].upper()+palabra[1:]
print(palabrasalida)