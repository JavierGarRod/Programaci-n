dias_semana=["Lunes","Martes","Jueves"]
#               0        1        2
dias_finde=["Sabado","Domingo"]
print(dias_semana[1:4]) #lectura por posicion del 1 hasta el 4 sin incluirlos
dias_semana.append("Viernes") #para introducir datos
dias_semana.insert(2,"Miercoles") #para introducir datos donde quiera
dias_semana=dias_semana+dias_finde #fusion de listas
print(dias_semana)


#LAS CADENAS SON INMUTABLES
mensaje="Lucía"
mensaje.replace("a","o") #remplaza en la lista mensaje TODAS las palabras "a" por "o"
print(mensaje)
mensaje=mensaje.replace("a","o") #Así se cambia el nombre
nombreLista=list(mensaje) #Paso de String a lista de caracteres
nombreLista.insert(0,"A")
print(nombreLista)
cadena=""
for valor in nombreLista: #Paso de lista de caracteres a String
    cadena=cadena+valor
print(cadena)


print(dias_semana[0:len(dias_semana)]) #imprime la lista completa
print(dias_semana[-len(dias_semana)]) #imprime solo el primero de la lista ya que elimina todos los demás
print(dias_semana[:-len(dias_semana)]) #imprime todo eliminado
print(dias_semana[::-1]) #imprime la lista al revés
dias_semana.pop(6) #para borrar por posicion
dias_semana.remove("Martes") #para borrar por valor
print(len(dias_semana)) #tamaño de la lista
print(dias_semana)


for dias in dias_semana: #para imprimir cada dato de la lista
    print(dias)
for dias in range (len(dias_semana)): #para imprimir cada dato de la lista
    print(dias)
for dias in reversed (dias_semana): #para imprimir cada dato de la lista de forma inversa
    print(dias)

if "martes2" in dias_semana:
    print("Lo tengo")
    print(dias_semana.index("Lunes")) #devuelve en que posicion esta ese valor
else:
    print("No lo tengo")


txt= "The best thing in life are free"
print("free" in txt) #averigua si "free" esta en la lista imprimiendo true
print("free" not in txt) #averigua si "free" no esta en la lista impromiendo true


dias2=["Bienvenidos a pepelandia"]
dias2.split("o") #Quita de la lista todo los elementos que sean en este caso "o"
print(dias2)