#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector

#conectar a base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='biblioteca',
    password='biblioteca',
    database='biblioteca',
)

mycursor = mydb.cursor()
#consultar en base de datos la lista de todos los camiones
sql="SELECT FROM socios"
mycursor.execute(sql)
myresult = mycursor.fetchall()



print("Content-Type: text/plain\n")
print('<html><head><meta charset="UTF-8"></head><body>')
print('<h2>Listado de libros prestados</h2>')

for socio in myresult:
    ids=socio[0]
    nombre=socio[1]

    print('<hr>')
    print('<h3>'+socio+'Ha recibido en prestamo/h3>')
    sql='SELECT titulo FROM libros where id_socio='+str(ids)
    mycursor.execute(sql)
    myresultLibros = mycursor.fetchall()

    for libro in myresultLibros:
        print('<p>'+libro[0]+'</p>')