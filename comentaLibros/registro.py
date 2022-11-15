#!C:\Users\alberto.turienzo\AppData\Local\Microsoft\WindowsApps\python

import cgi
import datetime
from http import cookies
import json
import os.path
import codigoHTML
import sys
import hashlib

args = cgi.parse()

datos = []

if "usuario" in args and "email" in args and "passwd" in args:
    user = args["usuario"][0]
    mail = args["email"][0]
    
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    passwd=h.hexdigest()

    mycursor = mydb.cursor()

    sql = 'SELECT COUNT(*) FROM usuarios where usuario like \"%s\"'

    mycursor.execute(sql)

    myresult = mycursor.fetchone()

    if myresult[1]==passwd:
        existe = True

if existe:
    coki = cookies.SimpleCookie()
    coki["SID"] = "alskdjfhg"
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)  
    coki['SID']['expires'] = expires.strftime("%a, %d, %b %Y %H :%M :%S GMT")
    print(coki)

    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=pagina1.py"/>', "Validado con exito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)
        
if not existe:
    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',"Usuario o contraseña no existen. Redirigiendo","",""))
    print(codigoHTML.finalHTML)
