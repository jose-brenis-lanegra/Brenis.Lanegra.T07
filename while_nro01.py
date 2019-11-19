#hallar el area de un triangulo, de base mayor a 136 y de altura menor a 359
import os
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
a=(base*altura)/2

#mientras lo invalido
while (base<=136 or altura>=359):
    base=float(input("ingrese la base:"))
    altura=float(input("ingrese la altura:"))
    a=(base*altura)/2
#fin_while
print("fin del bucle")
print("el area del triangulo es:", a)
