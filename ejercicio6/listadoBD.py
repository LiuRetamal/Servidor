#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector
import json

#conectar a base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='biblioteca',
    password='biblioteca',
    database='biblioteca',
)

mycursor = mydb.cursor()
#consultar en base de datos la lista de todos los camiones
sql="SELECT titulo, autor FROM libros"

mycursor.execute(sql)
lc = mycursor.fetchall()

print("Content-Type: text/plain\n")
print(json.dumps(lc))