#!C:\Users\alberto.turienzo\AppData\Local\Microsoft\WindowsApps\python

import cgi, os, sys
import json
import codigoHTML
from http import cookies
import datetime
import hashlib

args = cgi.parse()

existe = False

if "usuario" in args and "passwd" in args and os.path.exists("datos/usuarios.json"):
    
    usu = args["usuario"][0]
    h= hashlib.sha512(str.encode(args["passwd"][0]))
    passwd=h.hexdigest()
    
    mycursor = mydb.cursor()
    sql = 'SELECT id, passwd FROM usuarios where usuario like \"'+usu+'\"'
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

    sql = "UPDATE usuarios SET coki = '" +coki["SID"]+""
    mycursor.execute(sql)
    mydb.commit()

    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Entraste",'<meta http-equiv="Refresh" content="2; URL=pagina1.py"/>', "Validado con exito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)
        
if not existe:
    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Error", '<meta http-equiv="Refresh" content="2; URL=error.html"/>',"Usuario o contraseña no existen. Redirigiendo","",""))
    print(codigoHTML.finalHTML)