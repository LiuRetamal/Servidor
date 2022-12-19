#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi
import os
from http import cookies

form = cgi.FieldStorage()
if "puntos" in form:
    puntuacion = form['puntos'].value
else:
    puntuacion=""


if puntuacion == "BORRAR":
    coki = cookies.SimpleCookie()
    coki["punto"] += ""

else:

    todasCokis={}
    if 'HTTP_COOKIE' in os.environ:
        listaCoki = os.environ['HTTP_COOKIE']
        listaCoki = listaCoki.split('; ')

        for elemCoki in listaCoki:
            (nombre,valor) = elemCoki.split('=')
            todasCokis[nombre]=valor

    coki = cookies.SimpleCookie()
    coki["punto"] += 1

print("Puntos acumulados: "+todasCokis['punto'])


print("Content-Type: text/html\n")
print(todasCokis)
print("correcto")