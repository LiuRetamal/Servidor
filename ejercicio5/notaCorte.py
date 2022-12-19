#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi

fNombres = open("datos/nombres.dat", "rt")
fNotas = open("datos/notas.dat", "rt")


nombres = fNombres.read()
notas = fNotas.read()

fNombres.close()
fNotas.close()

nombres = nombres.split(" ")
notas = notas.split(" ")

form = cgi.FieldStorage()
corte = form['corte'].value

fSalida = open("datos/salida.dat","wt")

cont=0
for n in nombres:
    if notas[cont]>=corte:
        fSalida.write(n+" "+notas[cont]+"\n")
    cont+=1

fSalida.close()
print("Content-Type: text/html\n")

print("Filtro realizado...")





"""
EJERCICIO MAL

args = cgi.parse()
datos = []

if "corte" in args :
    datos.append(args["corte"][0])
    datos= []
    correcto= True    
    
    if(os.path.exists("datos/notas.dat")):
        f = open("datos/notas.dat", "rt")
        datos=f.read()
        f.close()
        
    elif (os.path.exists("datos/nombres.dat")):
        f = open("datos/nombres.dat", "rt")
        datos=f.read()
        f.close()
    else:
        f = open("datos/salida.dat", "w")    
        f.write(datos)
        f.close()

    


EJERCICIO ALEXANDER
nota = args["corte"][0]


readerNombres = open("datos/nombres.dat","r")
readerNotas = open("datos/notas.dat","r")

nombres = readerNombres.readline()
notas = readerNotas.readline()

nombres.split(" ")
notas.split(" ")

modificaFichero = open("datos/salida.dat","w")

for i in nombres:
    if nota>=notas[i]:
        modificaFichero.write(nombres[i]," ",notas[i])

print("Content-Type: text/html\n")

print("<!DOCTYPE html><html><head></head><body><p>Filtro realizado</p></body></html>")

"""