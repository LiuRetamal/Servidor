#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

"""
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

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre,valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

print("Content-Type: text/html\n")


print("""
<!DOCTYPE html>
<html>
    <head></head> 
    <body>  
""")

print("Palabras que empiezan por ABC: "+todasCokis['empiezaABC'])
print("Palabras que no empiezan por ABC: "+todasCokis['otras'])

print("""
    </body>
</html>
""")

















"""
EJERCICIO MAL
from http import cookies

print("Content-Type: text/html\n")
#inicio del codigo HTML#
print (cabeceraHtml.format("Cookies","Cookies"))

print("<p>Palabras que empiezan por ABC: </p>")
print("<p>Palabras que no empiezan por ABC: </p>")

#fin del codigo HTML#
print (finalHtml)
"""




