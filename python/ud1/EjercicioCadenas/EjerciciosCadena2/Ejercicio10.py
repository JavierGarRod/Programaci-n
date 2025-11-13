cadena=input("Dime una frase: ")
pal1=input("Dime una letra: ")
pal2=input("Dime otra letra: ")
if pal1.len()==0 and pal2.len() ==0:
    cadena=cadena.replace(pal1,pal2)
    print(cadena)