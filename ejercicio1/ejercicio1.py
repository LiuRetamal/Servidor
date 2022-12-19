#!C:\Users\alberto.turienzo\AppData\Local\Microsoft\WindowsApps\python
"""
Ejercicio 1:
    Escribe python que genere html. Dentro de carpeta imagen hay 20 imagenes.png.
    Usando un bucle sacar cada imagen dentro de un elemento div img. Cada div tiene atributo id con valores. 
    Cada img con atributo alt con valores.
crear html con 20 X div -> img
    div id="contenedorN"
        img src="cocheN.png" alt="img coche N"
"""

print("Content-Type: text/html\n")
print("""
<!DOCTYPE html>
<html>
    <head></head> 
    <body>     
            
""")
for n in range(1,21):
    print('<div id="contenedor'+str(n)+'">')
    print('     <img src="coche'+str(n)+'.png" alt="imagen de coche '+n+'">')
    print('</div')

print("""
    </body>
</html>
""")

for n in range(1,11):
    print('<a href="producto'+str(n)+'.html" title="Ir al producto'+str(n)+'">"Producto numero'+str(n)+'"')
    print('</a>')                          