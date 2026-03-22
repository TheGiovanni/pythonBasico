#tuplas
"""
Casos donde NO debes usar tuplas:

1 Cuando necesitas modificar, añadir o eliminar elementos → Usa listas
2 Cuando necesitas acceso por clave descriptiva → Usa diccionarios
3 Cuando necesitas operaciones complejas de búsqueda/filtrado → Usa
 listas o sets
Resumen:

Usa tuplas cuando necesites:

✅ Inmutabilidad garantizada
✅ Claves en diccionarios o elementos en sets
✅ Retorno múltiple de funciones
✅ Estructuras de datos que no cambiarán
✅ Mejor performance en iteraciones constantes
✅ Garantía de que los datos mantengan su estructura y orden
Las tuplas son tu elección cuando la integridad de los datos y la 
garantía de inmutabilidad son más importantes que la flexibilidad 
de modificación.
"""

# Tuplas en Python: ordenadas, inmutables y permiten elementos duplicados

hardware= ("CPU", "GPU", "RAM", "SSD", "HDD","CPU") #crea una tupla de hardware, permite duplicados
print(hardware) #imprime la tupla completa
print(type(hardware)) #imprime el tipo de dato de la variable hardware
print(hardware[0]) #imprime el primer elemento de la tupla (CPU)
print(len(hardware)) #imprime la cantidad de elementos en la tupla (6)
#la tupla es inmutable
#hardware[0]= "Procesador" #esto generará un error porque las tuplas no permiten modificar 
# sus elementos
#permite distintos tipos de datos
mi_tupla = ("Hola", 42, 3.14, True) #crea una tupla con distintos tipos de datos
print(mi_tupla) #imprime la tupla con distintos tipos de datos
print(type(mi_tupla)) #imprime el tipo de dato de la variable mi_tupla

x,y,z,a,b,c = hardware #desempaqueta la tupla hardware en variables individuales
print(x) #imprime el primer elemento de la tupla (CPU)
print(y) #imprime el segundo elemento de la tupla (GPU)
print(z) #imprime el tercer elemento de la tupla (RAM)
print(a) #imprime el cuarto elemento de la tupla (SSD)
print(b) #imprime el quinto elemento de la tupla (HDD)
print(c) #imprime el sexto elemento de la tupla (CPU)

tupla1= (1,2,3) #crea una tupla con números
tupla2 = ("uno", "dos", "tres") #crea una tupla con palabras
tupla3 = tupla2 + tupla1 #une las dos tuplas en una
print(tupla3) #imprime la tupla resultante de la unión de tupla1 y tupla2

for  h in hardware:
    print(h) #imprime cada elemento de la tupla hardware en una nueva línea

#un truco para modificar una tupla es convertirla a lista, modificar la lista 
# y luego convertirla de nuevo a tupla
hardware_lista = list(hardware) #convierte la tupla hardware a una lista
hardware_lista[0] = "Procesador" #modifica el primer elemento de la lista
hardware = tuple(hardware_lista) #convierte la lista de nuevo a tupla
print(hardware) #imprime la tupla actualizada con "Procesador" en lugar
# de "CPU"