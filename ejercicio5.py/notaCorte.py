#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")
import cgi
import os

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

    

