#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi, datetime, sys
import hashlib
import json
import codigoHTML
import os
from http import cookies

args = cgi.parse()
datos = []

existe = False

if "nombre" in args and "pass" in args and os.path.exists("daots/usuario.json"):

    datos.append(args["nombre"][0])
    datos.append(args["pass"][0])

    f = open("datos/usuario.json", "rt")
    datosJson=json.loads(f.read())       
    f.close()
    
    #escribir en log error
    for y in datosJson:
        for z in y:
            sys.stderr.write(">"+z+"<")
    
    for x in datosJson:
        datosNombre = x[0]
        datosEmail = x[1]
        datosPass = x[2]

        h=hashlib.sha512(str.encode(datos[1]))

        if datosNombre == datos[0] and datosPass == h.hexidigest():
            existe = True
            break


if existe:
    coki = cookies.SimpleCookie()
    coki['SID']="asdfgh"
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("entraste"))
    print(codigoHTML.finalHTML)

if not existe:
    print("Content-Type: text/html\n")

