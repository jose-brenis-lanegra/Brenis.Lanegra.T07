#hallar el area del trapecio si su bases se respetan y su altura sea igual de 74
import os
base_mayor=float(os.sys.argv[1])
base_menor=float(os.sys.argv[2])
altura=float(os.sys.argv[3])
area=(altura*(base_mayor+base_menor))/2

#mientras lo invalido
while (base_mayor<=base_menor or altura!=74):
    base_mayor = float(input("ingrese base mayor:"))
    base_menor = float(input("ingrese base menor:"))
    altura = float(input("ingrese altura:"))
    area= (altura * (base_mayor + base_menor)) / 2

#fin_while
print("fin del bucle")
print("el area del trapecio es:", area)
