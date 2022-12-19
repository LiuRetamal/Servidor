#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python
""""
Ejercicio 4:
    En "separaABC.py" se recibe el parámetro del formulario "texto". Se usan dos cookies, coki["empiezaABC"]=
    coki["otras"]; en la 1ª cookie se irán concatenando las palabras q empicen por ABC separadas por espacios en blanco y en la otra el resto.
    En caso de recibir cadena vacía, as dos cookies se reinician con cadena vacías.
    Otro python "muestraABC.py" genera HTML con contenido de las cookies con mensajes "Palabras que empiezan por ABC" y "Palabras que no empiezan con ABC"
        <form action="separaABC.py" method="get" >
            <input type="text" name="texto" />
            <input type="submit" value="enviar" />
        </form>
"""
import cgi
import os
from http import cookies

form = cgi.FieldStorage()
if "texto" in form:
    palabra = form['texto'].value
else:
    palabra=""


if palabra == "":
    coki = cookies.SimpleCookie()
    coki["empiezaABC"] += ""
    coki["otras"] += ""

else:

    todasCokis={}
    if 'HTTP_COOKIE' in os.environ:
        listaCoki = os.environ['HTTP_COOKIE']
        listaCoki = listaCoki.split('; ')

        for elemCoki in listaCoki:
            (nombre,valor) = elemCoki.split('=')
            todasCokis[nombre]=valor

    coki = cookies.SimpleCookie()
    
    abc=""
    noAbc=""

    if (palabra[0]=="A" and palabra[1]=="B" and palabra[2]=="C"):
        abc=palabra
    else:
        noAbc=palabra

    if 'empiezaABC' in todasCokis:
        coki['empiezaABC']=todasCokis['empiezaABC'] +" " + abc
    else:
        coki['empiezaABC']=abc

    if 'otras' in todasCokis:
       
        coki['otras']=todasCokis['otras']+" " + noAbc
    else:
        coki['otras']=noAbc

print(coki)


print("Content-Type: text/html\n")
print(todasCokis)
print("correcto")




#VARIANTES
#print("empieza por ABC") if (palabra[:3]=="ABC") else print("No empieza por ABC")
"""
if (palabra[:3]=="ABC"):
    print("Empieza por ABC")
else:
    print("No empieza por ABC")

"""











"""
EJERCICIO MAL
import os
from http import cookies

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (texto,valor) = elemCoki.split('=')
        todasCokis[texto]=valor

coki = cookies.SimpleCookie()
coki["empiezaABC"]= "ABC"
coki["otras"]= "DEFGHIJKLMNÑOPQRSTUVWXYZ"
print(coki)

"""

