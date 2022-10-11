#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi
import codigoHTML
import os
from http import cookies


usuarios = {"pepe": ["1234", "asd"], "maria": ["1111", "dsa"]}

args = cgi.parse()
user = args ['usuario'][0]
passwd = args ['pass'][0]
estaDentro = False

if user in usuarios:
    if usuarios[user][0] == passwd:
        estaDentro=True

if estaDentro:
    coki = cookies.SimpleCookie()

    coki["SID"]=usuarios[user][1]
    print(coki)

print("Content-Type: text/html\n")

print(codigoHTML.cabeceraHTML.format("CNI", "Entrada al CNI"))

if estaDentro:
    print("<h6 class='Display-6'>Estas dentro</h6>")

print(codigoHTML.finalHTML)

