#conjuntos (sets) colección no ordenada de elementos únicos
#no se puede acceder por índices
#se usa corchetes {} o la función set()
#no permiten elementos duplicados
#son mutables, pero no se pueden modificar los elementos individuales, solo agregar o eliminar

colores = {"Rojo", "Verde", "Azul", "Amarillo", "Rojo"} #crea un conjunto de colores, no imprime el ultimo rojo
print(colores) #imprime el conjunto completo, sin duplicados
print(type(colores)) #imprime el tipo de dato de la variable colores
print(len(colores)) #imprime la cantidad de elementos únicos en el conjunto colores
print("------------------------------------")

conjuntos = {1, "verde", 3.14, True} #crea un conjunto con diferentes tipos de datos
print(conjuntos) #imprime el conjunto completo
for i in conjuntos: #itera sobre cada elemento del conjunto conjuntos
    print(i) #imprime cada elemento del conjunto en una nueva línea, el orden no es garantizado

print("------------------------------------")

print ("rojo" in colores) #verifica si "rojo" está en el conjunto colores, devuelve 
#False porque es case-sensitive
print ("Rojo" in colores) # True

print("------------------------------------")

#agregar elementos
colores.add("Naranja")
print(colores) #imprime el conjunto colores con el nuevo elemento "Naranja"
#agregar mas de un elemento
colores.update(["Morado", "Cyan"])
print(colores) #imprime el conjunto colores con los nuevos elementos "Morado" y "Cyan"

#Eliminar elememtos
colores.remove("Verde") #elimina el elemento "Verde" del conjunto colores
print(colores) #imprime el conjunto colores sin el elemento "Verde"
colores.discard("Amarillo") #elimina el elemento "Amarillo" del conjunto colores, no genera error si el elemento no existe
print(colores) #imprime
#colores.pop() #elimina un elemento aleatorio del conjunto colores
#print(colores) #imprime el conjunto colores sin el elemento eliminado por pop()
colores.clear() #elimina todos los elementos del conjunto colores
print(colores) #imprime el conjunto colores vacío


print("------------------------------------")

#operaciones con conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print( f"conjunto A: {A}") #imprime el conjunto A
print(f"conjunto B: {B}") #imprime el conjunto B
#union
c = A.union(B)#crea un nuevo conjunto c que contiene todos los elementos de A y B, sin duplicados
print(f"Unión: {c}") #imprime el conjunto c que es la unión de A y B
#intersección
d = A.intersection(B) #crea un nuevo conjunto d que contiene solo los elementos que están en ambos conjuntos A y B
print(f"Intersección: {d}") #imprime el conjunto d que es la intersección de A y B
#diferencia
e = A.difference(B) #crea un nuevo conjunto e que contiene los elementos que están en A pero no en B
print(f"Diferencia A-B: {e}") #imprime el conjunto e que es la diferencia de A y B
f = B.difference(A) #crea un nuevo conjuntof que contiene los elementos que están en B pero no en A
print(f"Diferencia B-A: {f}") #imprime el conjunto f que es la diferencia de B y A