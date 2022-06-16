from telnetlib import theNULL


#numeros = -10
#val2 = 3

#if numeros >0:
#    print("El numero es positivo")
#else:
#    print("el numero es negativo")

print("Escriba un numero positivo o negativo")
numeros = int(input())
if numeros > 0:
     print("El numero es positivo")
if (numeros % 2) == 0:
    print("Este numero es par")
else:
    print("Este numero es negativo")