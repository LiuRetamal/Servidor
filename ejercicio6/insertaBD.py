#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi
import sys
import mysql.connector

form = cgi.FieldStorage()
#obtengo el nombre del socio, el titulo y el autor y Compruebo si existe el parametro
if "socio" in form and "titulo" in form and "autor" in form:
  socio = form ['socio'].value
  titulo = form['titulo'].value
  autor = form['autor'].value

  #conectar a la base de datos
  mydb = mysql.connector.connect(
  host='localhost',
  user='biblioteca',
  password='biblioteca',
  database='biblioteca'
  )

  mycursor = mydb.cursor()
  sql='SELECT id FROM socios where nombre like '+socio+''
  mycursor.execute(sql)
  myresult=mycursor.fetchone()
  
  if mycursor.rowcount == 1:
    ids= myresult[0]
    
    sql='INSERT INTO libros(numAdultos, numMenores, id_comprador) VALUES(%s,%s,%s)' 
    val=(numAdultos, numMenores,ids)
    mycursor.execute(sql,val)
    mydb.commit()

    salida="Libro Prestado"
  else:
    salida="Socio no existe"

else:
  salida="Error. Falta un parámetro"

print("Content-Type: text/plain\n")
print(salida)








