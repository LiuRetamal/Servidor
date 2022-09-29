#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()

texto = args["cadena"][0]

print(texto)

print(len(texto))

for letra in texto:
    print(letra)

if "hola" in texto:
    print("hola esta en " + texto)

print(texto[2:10])
print(texto[:10])
print(texto[:2])

#revertir una frase
cadenaInvertida = texto[::-1]
print(cadenaInvertida)

