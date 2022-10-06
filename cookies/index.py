#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os
from http import cookies

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre,valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

coki = cookies.SimpleCookie()
coki["contador"]=0
coki["nombre"]="uwu"
print(coki)

print("Content-Type: text/html\n")
#inicio del codigo HTML#
print (codigoHTML.cabeceraHtml.format("Cookies","Cookies"))

print(todasCokis)

#fin del codigo HTML#
print (codigoHTML.finalHtml)
