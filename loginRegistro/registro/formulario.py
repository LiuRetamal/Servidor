#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi
import json
import os


args = cgi.parse()

datos = []

datos.append(args["nombre"][0])
datos.append(args["pass"][0])
datos.append(args["email"][0])

path = 'datos/usuario.json'

isExist = os.path.exists(path)

if (isExist == True):
    f = open("datos/usuario.json", "r")
    f.read(json.dumps(datos))
    f.close()
else:
    f = open("datos/usuario.json", "w")    
    f.write(json.dumps(datos))
    f.close()


