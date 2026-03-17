#match
dia = input("Ingresa un dia de lunes a viernes: ").lower()
match dia:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case "miercoles":
        print("Hoy es miercoles")
    case "jueves":
        print("Hoy es jueves")
    case "viernes":
        print("Hoy es viernes")
    case _:
        print("Dia no valido") #El guion bajo se utiliza como un comodín para indicar que no se cumple ninguna de las condiciones anteriores
