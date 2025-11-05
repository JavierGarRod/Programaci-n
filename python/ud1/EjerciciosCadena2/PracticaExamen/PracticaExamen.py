clientes = []

while True:
    print("===========================================================")
    print("A) Añadir cliente")
    print("V) Validar emails almacenados")
    print("C) Contar clientes de un dominio")
    print("M) Mostrar /% de clientes premium y normales")
    print("G) Salir")
    print("===========================================================")

    opcion = input("Seleccione una opción: ").upper()

    if opcion == "A":
        while True:
            tipo = input("¿Es cliente premium? (S/N): ").upper()
            if tipo in ['S', 'N']:
                False
            else:
                print("Respuesta inválida. Introduzca S o N.")
        email = input("Introduce el correo electrónico: ")
        clientes.append((email, tipo))
        print("Cliente añadido correctamente.")
        
    elif opcion == "V":
        incorrectos = []
        for email in clientes:
            if "@" not in email:
                incorrectos.append(email)
            else:
                parte_dominio = email.split("@", 1)[1]
                if "." not in parte_dominio:
                    incorrectos.append(email)
        print("VALIDACIÓN DE EMAILS:")
        print(f"Total de correos almacenados: {len(clientes)}")
        print(f"Correos incorrectos: {len(incorrectos)}")
        if incorrectos:
            print("Lista de emails incorrectos:")
            for e in incorrectos:
                print(" -", e)
        else:
            print("Todos los correos son válidos.")
        print()

    elif opcion =="M":
        print("Estamos trabajando en ello...")

    elif opcion == "G":
        print("Saliendo del programa. ¡Hasta pronto!")
        False

    else:
        print("Opción no válida. Intente de nuevo.")