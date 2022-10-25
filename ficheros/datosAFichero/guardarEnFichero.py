#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi
import json

args = cgi.parse()
datos = []

datos.append(args["nombre"][0])
datos.append(args["edad"][0])

f = open("datos/listado.json", "a")
f.write(json.dumps(datos))
f.close()




