#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import datetime, cgi

#Fecha de hoy
x = datetime.datetime.now() #Fecha actual
y = datetime.datetime(2000, 1, 26) #Fecha especificada

print("Content-Type: text/plain\n")

print(type(x)) #Typo de formato ->  <class 'datetime.datetime'>
print(x) #Fecha de X (ahora) ->  2022-11-23 12:32:38.529413
print(x.year) #Año de X -> 2022
print(x.strftime("%A"))  #Dia de la Semana de la fecha de X
print(x.strftime("%c")) #Fecha local de X (ahora) -> Wed Nov 23 12:37:44 2022

print(y) #Fecha de Y (mi cumple) -> 2000-01-26 00:00:00

#---------------------------EJERCICIOS------------------------------------#
print("--------------------------------------------------------")
#Ejercicio 1


#a) Current date and time
print("Current date and time: " ,x) #2022-11-23 12:49:03.088025
#b) Current year
print("Current year: ",x.year) #2022
#c) Month of year
print("Month of year: ",x.month) #11
print(x.strftime("%B")) #Mes nombre largo #Noviembre
print(x.strftime("%b")) #Mes nombre corto #Nov
#d) Week number of the year
print("Week number of the year: ",x.strftime("%W")) #Dia de la semana 
#e) Weekday of the week
print("Weekday of the week: ",x.strftime("%w")) #Dia de la semana
#f) Day of year
print("Day of year: ",x.strftime("%j")) #Dia del año en numero #47
#g) Day of the month
print("Day of the month : ",x.strftime("%d")) #Día del mes numero #23
#h) Day of week
print("Day of week: ",x.strftime("%A")) #Dia de la semana #3
print(x.strftime("%a")) #Dia de la semana #3

print("-----------------------------------------------------------------")
#Bisiesto o no Ejercicio 2
datosForm = cgi.FieldStorage()
fecha = datosForm["fecha"].value if "fecha" in datosForm else False

#Decir si es bisiesto o no
if fecha:
    fecha=fecha.split("-")
    dFecha = datetime.datetime(int(fecha[0]),12,31)
    if int(dFecha.strftime("%j"))==366:
        print("Es bisiesto")
    else:
        print("No es bisiesto")
else:
    print("Error")


print("-----------------------------------------------------------------")
#Ejercicio 4
#Write a Python program to get the current time in Python.
print(datetime.datetime.now().time())

print("-----------------------------------------------------------------")
#Ejercicio 5
#Write a Python program to subtract five days from current date.
from datetime import date, timedelta

dt = date.today() - timedelta(5)
dd = date.today() + timedelta(15)

print('Fecha Actual :',date.today())
print('5 dias antes de la Fecha Actual:',dt)
print('5 dias antes de la Fecha Actual:',dd) 

print("-----------------------------------------------------------------")
#Ejercicio 7
#Write a Python program to print yesterday, today, tomorrow. 
hoy = datetime.date.today()
ayer = hoy - datetime.timedelta(days = 1)
mañana = hoy + datetime.timedelta(days = 1) 
print('Hoy : ',hoy)
print('Ayer : ',ayer)
print('Mañana : ',mañana)

print("-----------------------------------------------------------------")
#Ejercicio 9
#5 siguientes dias desde hoy
for n in range(0, 6):
    print(date.today() +timedelta(n))

print("-----------------------------------------------------------------")
#Ejercicio 10  
#Añadir 5 segundos a la hora actual
print(datetime.datetime.now().time())
dm = datetime.datetime.now()+timedelta(seconds=5)
print(dm.time()) #Hora + 5segs