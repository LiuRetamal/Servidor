#!C:\Users\zx21student035\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

from ast import operator
import cgitb
cgitb.enable()
import cgi

args = cgi.parse()

input1 = args['num1'][0]   
num1 = int(input1)           

input2 = args['num2'][0]   
num2 = int(input2)          

operacion = args['oper'][0]


if operacion == '1':
    print(num1+num2)
elif operacion == '2':
    print(num1-num2)
elif operacion == '3':
    print(num1*num2)
elif operacion == '4':
    print(num1/num2)

