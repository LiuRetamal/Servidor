#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()


print("Vamos a dibujar un cuadrado de ", args["nfilas"][0], "asteriscos")

nfilas = int(args["nfilas"][0])
linea = ""

for i in range(nfilas):
    for j in range(nfilas):
        linea += "*"
    print(linea)
    linea = ""