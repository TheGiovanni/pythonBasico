from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        #mostrar menu cafeteria
        print("\n \n Bienvenido a la Cafetería")
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            pedir_cafe() 
        elif opcion == "2":
            ver_historial()
        #ver historial
        elif opcion == "3":
        #salir
            break
        else:
            print("Opción no válida, por favor selecciona una opción del menú")
if __name__ == "__main__":
    main()
