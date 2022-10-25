#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi, datetime
import codigoHTML
import os
from http import cookies


usuarios = {"pepe": ["1234", "asd"], "maria": ["1111", "dsa"]}

args = cgi.parse()
user = args ['usuario'][0]
passwd = args ['pass'][0]
estaDentro = False
estilo = args['estilo'][0]

if user in usuarios:
    if usuarios[user][0] == passwd:
        estaDentro=True

if estaDentro:
    coki = cookies.SimpleCookie()

    coki['SID']=usuarios[user][1]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

print("Content-Type: text/html\n")



if estaDentro:
    print(codigoHTML.cabeceraHTML.format("Login", "Bienvenido"))
    print("<h6 class='Display-6'>Estás dentro</h6>")
    
    print(codigoHTML.finalHTML)

