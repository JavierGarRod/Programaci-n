meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
temperaturas = []
print("Introduce la temperatura media de cada mes del año:")

for i in range(12):
    temp = int(input("Introduce la temperatura",meses[i]))
    temperaturas.append(temp)

print("Diagrama de temperaturas medias por mes:")
for i in range(12):
    print(meses[i],temperaturas[i]*"*","(",temperaturas[i],"ºC)" )
