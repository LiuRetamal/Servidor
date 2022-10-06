#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

import codigoHTML
import cgi

args = cgi.parse() #devuelve diccionario

print(args)
#args -> {"contador":[1]}
#entre llaves porque es un diccionario y entre corchetes porque es una lista

#iniciar contador a 0 o valor desde URL#
contadorLista = args.get("contador",[0])
contador=int(contadorLista[0])

#incremento del contador
contador=contador+1

#inicio del codigo HTML#
print (codigoHTML.cabeceraHtml.format("Contador Visitas","Contador"))

#print('<a href="contadorVisitas.py?contador='+str(contador)+'">Llevas '+str(contador)+' visitas</a><br>')

print('<p>Llevas '+str(contador)+' visitas</p><br>')

print('<form action="contadorVisistas.py" method="post">')
print('<input type="text" name="nombre">')
print('<input type="hidden" name="contador" value="' +str(contador)+ '">')
print('<button type="submit">Enviar</button>')
print('</form>')


#fin del codigo HTML#
print (codigoHTML.finalHtml)
