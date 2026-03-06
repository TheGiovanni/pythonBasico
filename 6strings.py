#método string
#len
animal = "Murcielago"
print(len(animal))

#in 
texto = "Hola, ¿cómo estás?"
incluida = "Hole" in texto
print(incluida) #esto imprime False
noIncluida = "Hole" not in  texto
print(noIncluida) #esto imprime True

#convertir a mayusculas o minusculas
mayusculas = texto.upper()
print(mayusculas) #esto imprime HOLA, ¿CÓMO ESTÁS
minusculas = texto.lower()
print(minusculas) #esto imprime hola, ¿cómo estás?

#espacios
nombre = "   Juan   "
print(nombre) #esto imprime "   Juan   "
nombreSinEspacios = nombre.strip()
print(nombreSinEspacios) #esto imprime "Juan"