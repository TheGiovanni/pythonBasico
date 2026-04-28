try:
    numero = 10/5
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir a entero")
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe")

