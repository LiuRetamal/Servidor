#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python


import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']

#Comprobar si el archivo se ha subido
if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    #print("<h3>", fileitem. filename, "</h3>")
    #print("<h3>",fn,"</h3>")

    open("img/"+fn, 'wb').write(fileitem.file.read())
    print('<img src="img/'+fn+'">')