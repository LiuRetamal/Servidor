#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML,os,cgi,json
import mysql.connector


#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='comentaLibros',
  password='comentaLibros',
  database='comentaLibros'
)

mycursor = mydb.cursor()

 #obtengo la imagen, el titulo y el comentario
form = cgi.FieldStorage()
marca = form['marca']
modelo = form['modelo'].value
precio = form['precio'].value
desc = form['desc'].value

resultado = True

sql='INSERT INTO camiones (marca, modelo, precio, descripcion, fechaCreacion) VALUES (%s,%s,%s,%s, now())'
val = (marca, modelo, precio, desc)
mycursor.execute(sql, val)
mydb.commit()

print("Content-Type: text/plain\n")
print(json.dumps(resultado))