ARCHIVOS_PEDIDOS = "pedidos.txt"

def ver_historial():
    print ("\n Historial de Pedidos: ")
    try:
        with open(ARCHIVOS_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(f"{i}. {pedido.strip()}")
            else:
                print("No se han realizado pedidos aún.")
    
    except FileNotFoundError:
    
        print("No se han realizado pedidos aún.")