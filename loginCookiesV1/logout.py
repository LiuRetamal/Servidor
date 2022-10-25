#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os, datetime
from http import cookies

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]= valor

if 'SID' in todasCokis:
    coki = cookies.SimpleCookie()
    #solo se ejecuta la primera vez que accede el usuario
    coki['SID']=todasCokis["SID"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) #enviar cookie caducada
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)


print("Content-Type: text/html\n")


print(codigoHTML.cabeceraHTML.format("CNI", "Saliste del sistema"))    
print("<a href='index.html'>Pagina de acceso</a><br>")
print(codigoHTML.finalHTML)

print(codigoHTML.redireccionIndex())