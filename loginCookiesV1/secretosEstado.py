#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os
from http import cookies

print("Content-Type: text/html\n")

usuarios = {"pepe": ["1234", "asd"], "maria": ["1111", "dsa"]}
estaDentro = False

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]= valor

agente = "nadie"


if 'SID' in todasCokis:
    for agen, datos in usuarios.items():
        if (datos[1] == todasCokis[nombre]):
            estasDentro = True
            agente=agen

if estasDentro:
    print(codigoHTML.cabeceraHTML.format("CNI", "Secretos de Estado"))
    print("<h3 class='Display-3'>Bienvenido, agente " + agente + "</h3>")
    print("<a href='login.py'>Volver</a><br>")
    print("<a href='logout.py'>Salir</a><br>")
    print(codigoHTML.finalHTML)
else: 
    print(codigoHTML.cabeceraHTML.format("CNI", "Error en el acceso"))
    print("<a href='index.html'>Pagina de acceso</a><br>")
    print(codigoHTML.finalHTML)