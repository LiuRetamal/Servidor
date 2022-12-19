#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python
"""
Ejercicio 3:
    preciosProductosID = {
    "CA132": 99.2,
    "CB231": 55.7,
    "CA332": 101.0,
    "CD563": 65.2,
    "CB838": 48.1
}

    El id del producto tiene que ser clave del array y el precio el value.
    Recorrer array con foreach para crear tabla HTML con cabecera identificador y precio en dos columnas.
    En la 1ª columnas los id, en la 2ª los precios. Añadir fila con total con la suma de precios.

"""

preciosProductosID = {
    "CA132": 99.2,
    "CB231": 55.7,
    "CA332": 101.0,
    "CD563": 65.2,
    "CB838": 48.1
}
print("Content-Type: text/html\n")
print("""
<!DOCTYPE html>
<html>
    <head></head> 
    <body>   
        <table>
            <tr><th>Identificado </th><th> Precio</th></tr>
""")

total=0
for elemento in preciosProductosID:
    print("<tr><td>"+elemento+"</td><td>"+str(preciosProductosID[elemento])+"</td></tr>")
    total += preciosProductosID[elemento]

print("<tr><td>Total</td><td>"+str(total)+"</td></tr>")

print("""
        </table>
    </body>
</html>
""")






"""EJERCICIO MAL


idProducto = preciosProductosID.keys()

precio = preciosProductosID.values()

productos = preciosProductosID.items()

for itm in productos:
    print(itm[0],itm[1])
    
print(sum(precio))
"""



marcasCorredor = {
    "1001" : ("KIPRUTO, RHONEX", 3469),
    "1002" : ("KIPLIMO, JACOB", 3457),
    "1003" : ( "KANDIE, KIBIWOTT",	3452),
    "1007" :  ("MUTISO, ALEXANDER", 3479),
    "1008" :  ("WANDERS, JULIEN", 3595),
    "1009" :  ("KIPLIMO, PHILEMON", 3491)
}
print("Content-Type: text/html\n")
print("""
<!DOCTYPE html>
<html>
    <head></head> 
    <body>   
        <table>
            <tr><th>DORSAL </th><th> CORREDOR</th></tr>
""")

for elemento in marcasCorredor:
    print("<tr><td>"+elemento+"</td><td>"+str(marcasCorredor[elemento])+"</td></tr>")
    
ganador = min(marcasCorredor[elemento][0], marcasCorredor[elemento][2])
print(' <p>"EL ganador de la carrera fue: "'+ganador+'</p>')

print("""
        </table>
    </body>
</html>
""")



