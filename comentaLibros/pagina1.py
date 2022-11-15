#!C:\Users\alberto.turienzo\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML,os,sys
from http import cookies
import json

estasDentro=False

todasCokis={} 
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split(';')
                                
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

coki = cookies.SimpleCookie()

if 'SID' in todasCokis:
    
            
if estasDentro:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Pagina 1","","Pagina 1",
                                         '<form action="pagina2.py" method="get"><button type="submit" class="btn btn-primary">Pagina 2</button></form>',
                                         '<form action="logout.py" method="get"><button type="submit" class="btn btn-primary">Log out</button></form>',"",""))
    print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',
              "No hay cookie","",""))
    print(codigoHTML.finalHTML)