#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi
from gettext import textdomain

args = cgi.parse()

texto = args["cadena"][0]
palabra = args["pBuscar"][0]

salida = " "

print("Ejercicios de cadenas")
print("Contar las letras de una frase")
print("======================")
print("Ejercicio 1")

print(texto.count(''))

print("\n======================")
print("Ejercicio 2")
print("Buscar una palabra dentro de una frase")

if palabra in texto:
    print("Encontrada")
else:
    print("No Encontrada")

print("\n======================")
print("Ejercicio 3")
print("Contar las veces que aparece una letra dentro de una frase")

lista = texto.split()
frecuencia = []

for i in lista:
    frecuencia.append(lista.count(i))

print(str(list(zip(lista, frecuencia))))


print("\n======================")
print("Ejercicio 4")
print("Contar todas las veces que aparecen las vocales en una frase por separado, número de a, número de e, etc...")

vocales = "aeiou"
texto = texto.casefold()

contador = {}.fromkeys(vocales,0)

def contar(texto, vocales):
	
    for i in texto:
        if i in contador:
            contador[i] += 1
	
    return contador
print(contar(texto, vocales))

print("\n======================")
print("Ejercicio 5")
print("Dividir una frase en palabras")

for x in texto.split():
    print(x)

print("\n======================")
print("Ejercicio 6")
print("Dar la vuelta a las palabras de una frase")

def reverse(texto):
    return ' '.join(list(map(lambda x: x[::-1], texto.split())))

print(reverse(texto))

