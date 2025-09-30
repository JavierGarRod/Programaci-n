x=float(input("Cuanto has sacado en tu examen "))
y=int(input("Cuantos días has asistido a clases "))
if x>=60 and y>=80:
    print("Estas aprobado")
elif x<60 and y>80 or x>60 and y<80:
    print("Tienes un criterio suspenso")
else:
    print("Estas suspenso")