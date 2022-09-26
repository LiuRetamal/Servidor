#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgitb
cgitb.enable()
import cgi

args = cgi.parse()
num = int((args['numero'][0]))
if num < 1 or num > 10:
    print("El número tiene que estar entre  y 10")
else:
    for i in range (1,11):    
        print(num, " * ", i," = ", num*i)

