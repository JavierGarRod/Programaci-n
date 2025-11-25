tiempo=input("Dime un tiempo: ")

def segundo_a_hms(segundos):

    horas=tiempo//3600
    min=tiempo//60
    segundos=tiempo

    return horas,"horas",min,"minutos",segundos,"segundos"

tiempo=int(tiempo)
print(segundo_a_hms(tiempo))