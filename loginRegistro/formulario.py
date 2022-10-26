#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python



import cgi, datetime, json, os, sys, hashlib
from http import cookies

args = cgi.parse()

datos = []

if "nombre" in args and "email" in args and "pass" in args:
    datos.append(args["nombre"][0])
    datos.append(args["email"][0])
    h=hashlib.sha512(str.encode(datos.append(args["pass"][0])))
    datos.append(h.hexdigest())

    datosJson= []
    correcto= True    
    
    if(os.path.exists("datos/usuario.json")):
        f = open("datos/usuario.json", "rt")
        datosJson=json.loads(f.read())       
        f.close()
        
    else:
        f = open("datos/usuario.json", "w")    
        f.write(json.dumps(datosJson))
        f.close()

    #escribir en log error
    for y in datosJson:
        for z in y:
            sys.stderr.write(">"+z+"<")
    
    for x in datosJson:
        datosNombre = x[0]
        datosEmail = x[1]
        datosPass = x[2]

        h=hashlib.sha512(str.encode(datos[1]))

        if datosNombre == datos[0] and datosPass == h.hexidigest():
            existe = True
            break

if existe:
    coki = cookies.SimpleCookie()

    coki["SID"]="asdfgh"
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

if not existe:
    print("Content-Type: text/plain\n")


