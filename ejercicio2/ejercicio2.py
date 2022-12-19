#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python
"""
Ejercicio 2:
    Funcion en py "concatenaVocales" recibe parametro con nombre letras
    lista = ["A","E","I","O","U","E"]; Es un list que contiene letras.
    Comprobar que tamaño de array es igual o menor q 5 y el contenido son solo las vocales en Mayusculas.
    Devolver letras concatenadas como string. Si falla alguna condicion, se devuelve string "error".

"""

# def concatenaVocales(letras):
#     salida=""
#     if (len(letras)>5):
#       return "error"
    
#     for lt in letras:
#         if lt != 'A' and lt != 'E' and lt != 'I' and lt != 'O' and lt != 'U':
#             return "error"
#         salida += 1
#     return salida

# print("Content-Type: text/html\n")
# print(concatenaVocales(['A','U'])) #AU
# print(concatenaVocales(['E','A','U','O']))#AEUO
# print(concatenaVocales['b','A']) #error
# print(concatenaVocales(['E','A','U','O','U','O','I']))#rror


def cuentaNumeros(frase):
    #Comprobar que la frase tiene menos de 100 caracteres
    if (len(frase)>=100):
      return "error"

    numeros= "0123456789"
    contador = {}.fromkeys(numeros,0)

    for i in frase:
        if i in contador:
            contador[i] += 1
    return contador+1

print("Content-Type: text/html\n")
print(cuentaNumeros("hola"))




























"""
EJERCICIO MAL
lista = ["A","E","I","O","U","E"];

def concatenaVocales(lista):
    if (len(lista)<=5):
        print(lista)
    else:
        print("error")
    

print(concatenaVocales)
"""


    


