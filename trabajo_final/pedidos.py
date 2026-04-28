ARCHIVOS_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige tu café: ")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Americano")
    print("5. Mocha")
    opcion = input("Selecciona una opción: ")
    cafes ={ 
        "1": "Espresso",
        "2": "Latte",
        "3": "Cappuccino",
        "4": "Americano",
        "5": "Mocha"
    }
    
    #return cafes.get(opcion, "Opción no válida")

    if opcion in cafes:
        print(f"Has pedido un {cafes[opcion]}")

        with open(ARCHIVOS_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{cafes[opcion]}\n")
    else:        
        print("Opción no válida, por favor selecciona una opción del menú")
