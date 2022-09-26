#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi

args = cgi.parse()


print(args['edad'][0])

print(type(args))
print(type(args['edad']))
print(type(args['edad'][0]))

edad = int((args['edad'][0]))

print(edad)
print(type(edad))
