#slice

texto = "Hola, ¿cómo estás?"
print(texto[0]) #esto imprime "H"
print(texto[7]) #esto imprime "c"

print(texto[:11]) #esto imprime "Hola, ¿cómo"
print(texto[12:18]) #esto imprime "cómo estás?"
Nombre = "Juan"
saludo = "Hola mi nombre es Giovanni"
print(saludo.replace("Giovanni", Nombre))#reemplaza el texto

#normalización de texto

texto2 = "En este TEXTO hay MAYUSCULAS y minusculas"
#encontrar "mayusculas"
encontrar = "mayusculas" in texto2
print(encontrar) #esto imprime False porque "mayusculas" no está en el texto2 debido a la diferencia de mayúsculas y minúsculas

#normalizar a minúsculas
texto_min= texto2.lower()
encontrar_minuscula = "mayusculas" in texto_min
print(encontrar_minuscula) #esto imprime True porque ahora "mayusculas" está en texto_min
