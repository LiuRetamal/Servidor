#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()



print("Dibujos con asteriscos: ")

nfilas = int(5) ##Variable global##
figura = int(args["figura"][0])
linea = ""
##Figura 1
#####Función Rombo con Asteriscos#####
def asteriscos (nf):
    

    linea = ""

    for i in range(nf):
        for k in range(nf-i-1):
            linea += " "
            
        for j in range(i+1): 
            linea += "* "    
        print(linea)    
        linea = ""

    linea = ""

    for i in range(nf, 0, -1):
        for k in range(nf-i):
            linea += " "         
        for j in range(i-1): 
            linea += " *"    
        print(linea)    
        linea = ""
#####Fin Función Rombo con Asteriscos#####
print("----------------------------------------------------------")

##Figura 2
#####Función Rombo con Números#####
def numeros (nf):
    
    linea = ""

    for i in range(nf):
        for k in range(nf-i-1):
            linea += " "
            
        for j in range(i+1): 
            linea += str(i+1)+ " "
        print(linea)    
        linea = ""

    linea = ""

    for i in range(nf, 0, -1):
        for k in range(nf-i):
            linea += " "         
        for j in range(i-1): 
            linea += " "+str(i-1)
        print(linea)    
        linea = ""
#####Fin Función Rombo con Números#####


##Figura 3
#####Función Rombo con letras#####
def letras (nf):
    letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y",""]
    
    linea = ""

    for i in range(nf):
        for k in range(nf-i-1):
            linea += " "
            
        for j in range(i+1): 
            linea += str(letra.length)+ " "
        print(linea)    
        linea = ""

    linea = ""

    for i in range(nf, 0, -1):
        for k in range(nf-i):
            linea += " "         
        for j in range(i-1): 
            linea += " "+str(letra.length)  
        print(linea)    
        linea = ""
#####Fin Función Rombo con Letras#####

match figura:
    case 1:
        asteriscos(nfilas)
    case 2:
        numeros(nfilas)
    case 3:
        letras(nfilas)
    case _:
        print("opcion no contemplada")