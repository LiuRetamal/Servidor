#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi
import codigoHTML
import os
from http import cookies


usuarios = {"pepe": "1234", "maria": "1111"}

print("Content-Type: text/html\n")

args = cgi.parse()
user = args ['usuario'][0]
passwd = args ['pass'][0]



print(codigoHTML.cabeceraHTML.format("CNI", "Entrada al CNI"))

if user in usuarios:
    if usuarios[user] == passwd:
        print("estas dentro")
    else: 
        print("sabemos donde vives, no te muevas, la policia va a tu casa")
else:
    print("usuario incorrecto")

print(codigoHTML.finalHtml)

