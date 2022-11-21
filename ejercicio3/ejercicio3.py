#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

preciosProductosID = {
    "CA132": 99.2,
    "CB231": 55.7,
    "CA332": 101.0,
    "CD563": 65.2,
    "CB838": 48.1
}
idProducto = preciosProductosID.keys()

precio = preciosProductosID.values()

productos = preciosProductosID.items()

for itm in productos:
    print(itm[0],itm[1])
    
print(sum(precio))