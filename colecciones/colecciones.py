#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

def sacaPorPantalla(fruta):
    print("esto es ",fruta)

lista = ["apple", 123, "cherry", True]

print(len(lista))

[print(x) for x in lista]
[print(type(x)) for x in lista]

[sacaPorPantalla(x) for x in lista]
#------------------------------------
#nuevaList = [x for x in fruit if "a" in x]

listaNumeros = [2,5,7,6,9,1,8,4,3,0]

listaMayores5 = [n for n in listaNumeros if n>5]
listaMenores5 = [n*100 for n in listaNumeros if n<=5]

print(listaMayores5)
print(listaMenores5)

def valor01(n):
    if (n>=5):
        return 1
    else:
        return 0

listaMI5en1 = [valor01(n) for n in listaNumeros if n < 5]

print(listaMayores5, listaMenores5, listaMI5en1)

