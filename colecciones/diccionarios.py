#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

persona = {
    "nombre": "Juan",
    "apellidos": "Lopez Lopez",
    "edad": 32,
    "pareja": True,
    "deportes":["surf", "skate", "futbol"]
}

print(persona)
print(type(persona))

print("La edad de ", persona["nombre"], "es ", persona["edad"])

persona["nombre"]="Jose"
persona["edad"]=25
print("La edad de ", persona["nombre"], "es ", persona["edad"])

print(persona["deportes"][1])

claves = persona.keys()

print(claves)

persona["altura"]=180

print(claves)

valores = persona.values()

print(valores)

listaDeTuplas = persona.items()

print(listaDeTuplas)

for itm in listaDeTuplas:
    print(itm[0],itm[1])

persona["peso"]=80