dias_semana=["Lunes","Martes","Jueves"]
dias_finde=["Sabado","Domingo"]
print(dias_semana[1:4]) #lectura por posicion del 1 hasta el 4 sin incluirlo
dias_semana.append("Viernes") #para introducir datos
dias_semana.insert(2,"Miercoles") #para introducir datos donde quiera
dias_semana=dias_semana+dias_finde #fusion de listas
print(dias_semana)
print(dias_semana[0:len(dias_semana)]) #lista completa
print(dias_semana[-len(dias_semana)]) #dia de la semana
print(dias_semana[:-len(dias_semana)]) #dia de la semana
dias_semana.pop(6) #para borrar por posicion
dias_semana.remove("Martes") #para borrar por valor
print(len(dias_semana)) #tamaño de la lista
print(dias_semana)

if "martes2" in dias_semana:
    print("Lo tengo")
    print(dias_semana.index("Lunes")) #devuelve en que posicion esta ese valor
else:
    print("No lo tengo")