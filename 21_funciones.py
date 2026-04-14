#funciones
# se utliza def para definir una función, seguido del nombre de la función y paréntesis que pueden contener parámetros
# el bloque de código dentro de la función se indenta
# las funciones pueden devolver un valor utilizando la palabra clave return 

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")

def saludar2 (name, lastname="n/a"):#la función saludar2 tiene dos parámetros, name y lastname, donde lastname tiene un valor predeterminado de una cadena vacía
    return f"Hola, {name} {lastname}"

mensaje = saludar2 ("Maria", "Gonzales")
print(mensaje)
mensaje2 = saludar2 ("Carlos") #se llama a la función saludar2 con solo un argumento, lo que hace que lastname tome su valor predeterminado de una cadena vacía
print(mensaje2)

def suma (a,b):
    return a + b

resultado = suma (2,2)
print(resultado)

def funcion():
    pass #la palabra clave pass se utiliza como un marcador de posición para indicar que no se ha implementado ningún código en la función aún

def resta(a,b):
    return a - b

def multiplicación(a,b):
    return a * b

def división(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

resultadoResta = resta (10,9)
resultadoMultiplicación = multiplicación (5,5)
resultadoDivisión = división (10,2)
print(f"resultado de la resta: {resultadoResta}")
print(f"resultado de la multiplicación: {resultadoMultiplicación}")
print(f"resultado de la división: {resultadoDivisión}")

