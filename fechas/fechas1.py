#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import datetime,cgi
datosForm = cgi.FieldStorage()

#imprimir fecha del input
fecha = datetime.datetime(datosForm["fecha"].value) if "fecha" in datosForm else datetime.datetime.now()

print("Content-Type: text/plain\n")
print(fecha)

