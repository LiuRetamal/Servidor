#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi

fAlumnos = open("datos/datos.dat", "rt")

alumnos = fAlumnos.read()

fAlumnos.close()

alumnos = alumnos.split(" ")

form = cgi.FieldStorage()

fAprobados= open("datos/aprobados.dat","wt")
fSuspensos= open("datos/suspensos.dat","wt")

cont=0
for n in alumnos:
    if alumnos >= 5:
        fAprobados.write(n+" "+alumnos[cont]+"\n")
    else:
        fSuspensos.write(n+" "+alumnos[cont]+"\n")
    cont+=1

fAprobados.close()
fSuspensos.close()
print("Content-Type: text/html\n")

print("Separacion realizado...")

