#lambda
#Es una función anónima, es decir, no tiene un nombre específico.
#  Se utiliza para crear funciones pequeñas y de una sola línea.
# La sintaxis de una función lambda es la siguiente:
# lambda argumentos: expresión

def funcion(n):
    return lambda a : a* n

doble = funcion(2)
triple = funcion(3)
cuatruple = funcion(4)
print(doble(5)) # Salida: 10
print(triple(5)) # Salida: 15
print(cuatruple(5)) # Salida: 20
