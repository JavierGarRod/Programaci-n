meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
temperaturas = []
print("Introduce la temperatura media de cada mes del año:")

for mes in meses:
    temp = float(input(f"Temperatura media de {mes}: "))
    temperaturas.append(temp)

print("\nDiagrama de temperaturas medias por mes:")
for i in range(12):
    print(f"{meses[i]:<12}: ({temperaturas[i]}°C)")

    