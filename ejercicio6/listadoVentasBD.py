#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector

#conectar a base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='museo',
    password='museo',
    database='museo',
)

mycursor = mydb.cursor()
#consultar en base de datos la lista de todos los compradoress
sql="SELECT FROM comprador"
mycursor.execute(sql)
myresult = mycursor.fetchall()



print("Content-Type: text/plain\n")
print('<html><head><meta charset="UTF-8"></head><body>')
print('<h2>Listado de Ventas</h2>')

for comprador in myresult:
    ids=comprador[0]
    nombre=comprador[1]

    print('<hr>')
    print('<h3>'+comprador+'Ha comprado las siguientes: </h3>')
    sql='SELECT numAdultos, numMenores, total FROM entradas where id_comprador='+str(ids)
    mycursor.execute(sql)
    myresultCompra = mycursor.fetchall()
    

    for entradas in myresultCompra:
        print('<p>'+numAdultos[0]+' de adultos'+numMenores[0]+' de menores por'+total+' euros</p>')