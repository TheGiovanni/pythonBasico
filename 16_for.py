palabra = "Murcielago"

for letra in palabra:
    print(letra.upper()) #imprime cada letra en mayúscula


frutas = ["Naranja" ,"Kiwi", "Sandia"]
for fruta in frutas:
    if fruta == "Kiwi":
        print(fruta.upper()) #imprime "KIWI" en mayúscula
    else:   
        print(fruta.lower()) #imprime cada fruta en minúscula

print("--------------------------")

for i in range(10): #comienza en el cero y termina en 9
    print(i) #imprime los números del 0 al 9
print("--------------------------")

for i in range (1,11): #comienza en el 1 y termina en el 10
    print(i) #imprime los números del 1 al 10
print("--------------------------")

for i in range  (1, 11, 2): #comienza en el 1, termina en el 10 y salta de 2 en 2
    print(i) #imprime los números impares del 1 al 10
print("--------------------------")


for i in range  (2, 11, 2): #comienza en el 2, termina en el 10 y salta de 2 en 2
    print(i) #imprime los números pares del 2 al 10
print("--------------------------")


adjetivos = ["Deliciosa", "Dulce", "Jugosa"]
frutas = ["Naranja" ,"Kiwi", "Sandia"]
for fruta in frutas:
    for adjetivo in adjetivos:
        print(f"La {fruta} es {adjetivo}") #imprime cada fruta con cada adjetivo

print("--------------------------")

