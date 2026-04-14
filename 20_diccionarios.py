#Diccionarios

#Definición de un diccionario
#se usa la sintaxis de llaves {} o la función dict()
#los diccionarios almacenan pares clave-valor
#son mutables, lo que significa que se pueden modificar después de su creación

auto = {"Marca": "Toyota",
        "Modelo": "Corolla",
        "Año": 2025,
        "Color": "Rojo"}
print(auto) #imprime el diccionario completo
print(type(auto)) #imprime el tipo de dato de la variable auto
print(len(auto)) #imprime la cantidad de pares clave-valor en el diccionario auto
print("------------------------------------")
print (auto["Marca"])#imprime el valor asociado a la clave "Marca" en el diccionario auto
print (auto["Modelo"])#imprime el valor asociado a la clave "Modelo" en el diccionario auto
print (auto["Año"])#imprime el valor asociado a la

print(auto.get("Color"))#imprime el valor asociado a la clave "Color" en el diccionario auto, devuelve None si la clave no existe
print(auto.get("Precio", "No disponible"))#imprime el valor asociado a la clave"Precio" en el diccionario auto, devuelve "No disponible" si la clave no existe
print("------------------------------------")
print(auto.keys()) #imprime las claves del diccionario auto
print(auto.values()) #imprime los valores del diccionario auto
print(auto.items()) #imprime los pares clave-valor del diccionario auto como tuplas
print("------------------------------------")

if "Vendido" in auto:
    print("La clave 'Vendido' existe en el diccionario auto") #verifica si la clave "Vendido" existe en el diccionario auto, imprime un mensaje si es verdadero
else:
    print("La clave 'Vendido' no existe en el diccionario auto") #imprime un mensaje si la clave "Vendido" no existe en el diccionario auto

#Agregar o modificar elementos
auto["Modelo"]= "Camry" #modifica el valor asociado a la clave "Modelo" en el diccionario auto
print(auto) #imprime el diccionario auto con el valor modificado para la clave "
auto["Vendido"] = False #agrega un nuevo par clave-valor al diccionario auto con la clave "Vendido" y el valor False
print(auto) #imprime el diccionario auto con el nuevo par clave-valor agregado

print(auto.update({"Año": 2026,"Color": " Negro", "Puertas": "5"}))#modifica los valores asociados a las claves "Año" y "Color" en el diccionario auto utilizando el método update()
print(auto) #imprime el diccionario auto con los valores modificados para las claves "
print("------------------------------------" )
#Eliminar elementos
print(auto.pop("Puertas")) #elimina el par clave-valor asociado a la clave "Puertas" del diccionario auto y devuelve el valor eliminado
print(auto) #imprime el diccionario auto después de eliminar el par clave-valor asociado a la clave "Puertas"
print(auto.pop("Precio", "No disponible")) #intenta eliminar el par clave-valor asociado a la clave "Precio" del diccionario auto, devuelve "No disponible" si la clave no existe
print(auto) #imprime el diccionario auto después
del auto["Vendido"] #elimina el par clave-valor asociado a la clave "Vendido" del diccionario auto utilizando la palabra clave del
print(auto) #imprime el diccionario auto después de eliminar el par clave-valor asociado
#print(auto.clear()) #elimina todos los pares clave-valor del diccionario auto utilizando el método clear()
#print(auto) #imprime el diccionario auto después de eliminar todos los pares clave-valor
print("------------------------------------")
print("------------------------------------")
#recorrer un diccionario
for clave in auto:
    print(clave) #imprime cada clave del diccionario auto
print("------------------------------------")
for valor in auto.values():
    print(valor)#imprime cada valor del diccionario auto
print("------------------------------------")
print("------------------------------------")
for clave, valor in auto.items():
    print(f"{clave}: {valor}") #imprime cada par clave-valor del diccionario auto en formato "clave: valor"

print("------------------------------------")
print("------------------------------------")
#diccionarios anidados
persona = {
"persona1": {
    "Nombre": "Juan",
    "Edad": 30,
    "Ciudad": "Madrid"

},
"persona2":{
    "Nombre": "María",
    "Edad": 25,
    "Ciudad": "Barcelona"

},
"persona3":{
    "Nombre": "Pedro",
    "Edad": 35,
    "Ciudad": "Valencia"
}
}
print(persona) #imprime el diccionario persona completo
print(persona["persona1"]) #imprime el diccionario asociado a la clave "persona1" en el diccionario persona
print(persona["persona2"]["Nombre"]) #imprime el valor asociado a la clave "Nombre" en el diccionario asociado a la clave "persona2" en el diccionario persona
print(persona["persona3"]["Ciudad"]) #imprime el valor asociado a la clave "Ciudad" en el diccionario asociado a la clave "persona3"