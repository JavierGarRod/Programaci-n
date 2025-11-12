total_incidentes = 0
incidentes_leves = 0
incidentes_graves = 0
incidentes_eso = 0
incidentes_post = 0

registro=True

while registro:
    registrar = input("¿Desea registrar un nuevo incidente? (S/N): ").upper()
    level=True
    type=True

    if registrar == "N":
        registro=False
    elif registrar == "S":    
        while level:
            nivel = input("¿En qué nivel ha ocurrido? (E=ESO / P=Post-Obligatoria): ").upper()
            if nivel in ["E", "P"]:
                level=False
            else:
                print("Valor no válido. Introduzca E o P.")

        while type:
            tipo = input("Tipo de incidente (L=Leve / G=Grave): ").upper()
            if tipo in ["L", "G"]:
                total_incidentes += 1
                if tipo == "L":
                    incidentes_leves += 1
                else:
                    incidentes_graves += 1

                if nivel == "E":
                    incidentes_eso += 1
                else:
                    incidentes_post += 1
                type=False
            else:
                print("Valor no válido. Introduzca L o G.")
    else:
        print("Formato no válido")

print("Incidentes registrados.")

if total_incidentes > 0:
    porcentaje_eso = (incidentes_eso / total_incidentes) * 100
    porcentaje_post = (incidentes_post / total_incidentes) * 100

    print(f"Se han producido {total_incidentes} incidentes en el centro: "
          f"{incidentes_leves} de ellos Leves y {incidentes_graves} Graves, "
          f"siendo el {porcentaje_eso}% en ESO y el {porcentaje_post}% en Post-Obligatoria.")
else:
    print("No se registraron incidentes.")