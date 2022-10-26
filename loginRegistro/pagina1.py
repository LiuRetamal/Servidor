#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import json, sys, os
import codigoHTML
from http import cookies

sys.stderr.write("DENTRO DE PAGINA 1")

estasDentro=False

f = open("datos/usuario.json", "rt")
datosJson=json.loads(f.read())       
f.close()

todasCokis={}

if'HTTP_COOKIE' in os.environ:
    lisaCoki = os.environ['HTTP_COOKIE']
    lisaCoki = lisaCoki.split(';')

    for elemCoki in lisaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor
        
coki = cookies.SimpleCookie()

if 'SID' in todasCokis:
    for datos in datosJson:
        sys.stderr.write(">"+"asdfgh"+datos[2]+"<")