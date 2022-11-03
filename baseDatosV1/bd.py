#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector



#conectar a la base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='generico',
    password='generico',
    database='generico'
)

cantRegistros = 5

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM tabla")

#sentencia de sql 
sql = 'INSERT INTO tabla (columna1, columna2, columna3) VALUES (%s, %s, %s)'
for i in range(cantRegistros):
    #introducir valores
    val = ('valor uwu'+str(i), 'valor owo'+str(i), i)
    #inserta los datos en la tabla
    mycursor.execute(sql, val) 

mydb.commit()

print("Content-Type: text/plain\n")

mycursor.execute("SELECT * FROM tabla")

myresult = mycursor.fetchall()

print(type(myresult))

for x in myresult:
    print(x[0],"-",x[1],"-",x[2],"-",x[3])

mycursor.execute("SELECT count(*) FROM tabla")

myresult = mycursor.fetchone()

print(type(myresult))
print(myresult[0])