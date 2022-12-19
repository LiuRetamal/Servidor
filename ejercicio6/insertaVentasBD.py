#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi
import sys
import mysql.connector

form = cgi.FieldStorage()
#obtengo el dni del comprador, el numero de adultos y menores y Compruebo si existe el parametro
if "dni" in form and "adultos" in form and "menores" in form:
  comprador = form ['dni'].value
  numAdultos = form['adultos'].value
  numMenores = form['menores'].value

  #conectar a la base de datos
  mydb = mysql.connector.connect(
  host='localhost',
  user='museo',
  password='museo',
  database='museo'
  )

  mycursor = mydb.cursor()
  sql='SELECT dni FROM comprador where nombre like '+comprador+''
  mycursor.execute(sql)
  myresult=mycursor.fetchone()
  
  if mycursor.rowcount == 1:
    ids= myresult[0]
    
    sql='INSERT INTO entradas(numAdultos, numMenores, id_comprador) VALUES(%s,%s,%s)' 
    val=(numAdultos,numMenores,ids)
    mycursor.execute(sql,val)
    mydb.commit()

    total= (numAdultos*20) + (numMenores*5)
    salida="Venta realizada"
  else:
    salida="Venta no existente"

else:
  salida="Error. Falta un parámetro"

print("Content-Type: text/plain\n")
print(salida)
