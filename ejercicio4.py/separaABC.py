#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

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
