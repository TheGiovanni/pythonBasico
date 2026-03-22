# Listas en Python: ordenadas, mutables y permiten elementos duplicados

#indices   0           1       2        3       4
frutas = ["Naranja" ,"Kiwi", "Sandia", "Pera", "Manzana"] #crea una lista de frutas
print(frutas) #imprime la lista completa
print(type(frutas)) #imprime el tipo de dato de la variable frutas
print(frutas[0]) #imprime el primer elemento de la lista (Naranja)

#la lista es mutable

frutas[0]= "Limón" #cambia el primer elemento de la lista a "Limón"
print(frutas) #imprime la lista actualizada con "Limón" en lugar de "Naranja"
print(len(frutas)) #imprime la cantidad de elementos en la lista (5)
#permite duplicados
frutas.append("Kiwi") #agrega "Kiwi" al final de la lista, permitiendo un duplicado
print(frutas) #imprime la lista con el nuevo "Kiwi" al final
print(len(frutas)) #imprime la cantidad de elementos en la lista (6)
#permite distintos tipos de datos
mi_lista = ["Hola", 42, 3.14, True] #crea
print(mi_lista) #imprime la lista con distintos tipos de datos

#saber si el elemento existe en la lista

frutita= "Limón"
if frutita in frutas:
    print(f"La fruta: {frutita} está en la lista") #imprime si la variable está en la lista
else:
    print(f"La fruta: {frutita} no está en la lista") #imprime si la variable no está en la lista

#métodos de listas
frutas.append("Melón") #agrega "Melón" al final de la lista
print(frutas) #imprime la lista con "Melón" al final
frutas.insert(2, "Fresa") #inserta "Fresa" en la posición 2 de la lista
print(frutas) #imprime la lista con "Fresa" en la posición 2
frutas.remove("Kiwi") #elimina la primera aparición de "Kiwi" de la lista
print(frutas) #imprime la lista sin el primer kiwi
frutas.remove("Kiwi")
print(frutas) #imprime la lista sin el segundo kiwi
frutas.pop() #elimina el último elemento de la lista (Melón)
print(frutas) #imprime la lista sin "Melón"
frutas.pop(0) #elimina el elemento en la posición 0 (Limón)
print(frutas) #imprime la lista sin "Limón"
frutas.sort() #ordena la lista alfabéticamente
print(frutas) #imprime la lista ordenada alfabéticamente
frutas.reverse() #invierte el orden de la lista
print(frutas) #imprime la lista con el orden invertido
#frutas.clear() #elimina todos los elementos de la lista
#print(frutas) #imprime la lista vacía

#unir listas
mas_frutas = ["Mango", "Papaya"] #crea una nueva lista de frutas
todas_las_frutas = frutas + mas_frutas #une las dos listas en una nueva lista
print(todas_las_frutas) #imprime la lista con todas las frutas

frutas.extend(mas_frutas) #agrega los elementos de mas_frutas al final de la lista frutas
print(frutas) #imprime la lista frutas con los elementos de mas_frutas al final
#la lista frutas ahora contiene todas las frutas, incluyendo las de mas_frutas