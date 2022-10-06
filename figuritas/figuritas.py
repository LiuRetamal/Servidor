#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()



print("Dibujos con asteriscos: ")


nfilas = int(args["nfilas"][0]) ##Variable global##
figura = int(args["figura"][0])
linea = ""

##Figura 1
#####Función cuadrado#####
def cuadrado(nf):
    print("Cuadrado de ", args["nfilas"][0], "asteriscos")

    linea = ""

    for i in range(nf): #i -> 0, 1, 2, 3, 4
        for j in range(nf): #j -> 0, 1, 2, 3, 4
            linea += "*"
        print(linea)
        linea = ""


#####Fin Función cuadrado#####

print("----------------------------------------------------------")

##Figura 2
#####Función triangulo normal#####
def trianguloN(nf):
    print("Triangulo normal de ", args["nfilas"][0], "asteriscos")

    linea = ""

    for i in range(nf):  # i -> range(5) 0, 1, 2, 3,4
        for j in range(i+1): # i -> 0 range(0) nada
            linea += "*"    # i -> 1 range(1) 0
        print(linea)
        linea = ""

#####Fin Función triangulo#####

print("----------------------------------------------------------")

##Figura 3
#####Función triangulo con vuelta#####
def trianguloV (nf):
    print("Triangulo normal con vuelta de ", args["nfilas"][0], "asteriscos")

    linea = ""

    for i in range(nf, 0, -1):  # i -> range(5, -1, -1) 5, 4, 3, 2, 1
        for j in range(i): # i -> 0 range(0) nada
            linea += "*"    # i -> 1 range(1) 0
        print(linea)
        linea = ""

#####Fin Función triangulo con vuelta#####

print("----------------------------------------------------------")

##Figura 4
#####Función triangulo al reves#####
def trianguloR (nf):
    print("Triangulo normal al reves de ", args["nfilas"][0], "asteriscos")

    linea = ""

    for i in range(nf):
        for k in range(nf-i-1):
            linea += " "
            
        for j in range(i+1): 
            linea += "*"    
        print(linea)    
        linea = ""

#####Fin Función triangulo al reves#####

print("----------------------------------------------------------")

##Figura 5
#####Función triangulo al reves con vuelta#####
def trianguloRV (nf):
    print("Triangulo normal al reves con vuelta de ", args["nfilas"][0], "asteriscos")
    
    linea = ""

    for i in range(nf, 0, -1):
        for k in range(nf-i):
            linea += " "         
        for j in range(i): 
            linea += "*"    
        print(linea)    
        linea = ""

#####Fin Función triangulo al reves con vuelta#####

match figura:
    case 1:
        cuadrado(nfilas)
    case 2:
        trianguloN(nfilas)
    case 3:
         trianguloV(nfilas)
    case 4:
        trianguloR(nfilas)
    case 5:
        trianguloRV(nfilas)
    case _:
        print("opcion no contemplada")
