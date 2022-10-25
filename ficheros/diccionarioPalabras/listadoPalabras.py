#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")
from ast import For
import json

f = open("datos/listado.dat", "wt")

datosEnJson = json.loads(f.read())
f.close()

tam = len(datosEnJson)

for i in range (tam):
    print(i, ":",datosEnJson[i])

for elemento in datosEnJson:
    print(elemento[0], "---", elemento[1])