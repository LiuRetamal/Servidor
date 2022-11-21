#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import cgi,json
import mysql.connector


#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='biblioteca',
  password='biblioteca',
  database='biblioteca'
)

mycursor = mydb.cursor()

#obtengo el nombre del socio, el titulo y el autor
form = cgi.FieldStorage()
nombre = form ['socio'].value
titulo = form['titulo'].value
autor = form['autor'].value

if (form['socio'].value == False):
    print("El socio no existe")

resultado = True

sql='INSERT INTO libros (titulo, autor, id_socios) VALUES (%s,%s,%s)'
val = (nombre, titulo, autor)
mycursor.execute(sql, val)
mydb.commit()

print("Content-Type: text/plain\n")
print(json.dumps(resultado))

