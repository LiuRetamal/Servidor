#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgitb
cgitb.enable()
import cgi
import random

args = cgi.parse()
opcion = int((args['opcion'][0]))

if opcion == 1:
    print("has elegido piedra")
elif opcion == 2:
    print("Has elegido papel")
elif opcion == 3:
    print("Has elegido tijeras")


ordenador = random.randint(1,3)
if ordenador == 1:
    print("El ordenador elige: piedra")
elif ordenador == 2:
    print("El ordenador elige: papel")
elif ordenador == 3:
    print("El ordenador elige: tijeras")



if opcion == 1 and ordenador ==1:
    print("Empate")
elif opcion == 2 and ordenador == 2:
    print("Empate")
elif opcion == 3 and ordenador ==3:
    print("Empate")

if opcion == 1 and ordenador ==2:
    print("Gana el ordenador")
elif opcion == 1 and ordenador == 3:
    print("Ganas tu")
elif opcion == 2 and ordenador == 1:
    print("Ganas tu")  
elif opcion == 2 and ordenador == 3:
    print("Ganas el ordenador") 
elif opcion == 3 and ordenador == 1:
    print("Ganas el ordenador") 
elif opcion == 3 and ordenador == 2:
    print("Ganas tu") 