#hallar el area del rombo si sus diagonales se respetan
import os
dme=float(os.sys.argv[1])
dma=float(os.sys.argv[2])
a=(dma*dme)/2

#mientras lo invalido
while (dma<=dme):
    dme = float(input("ingrese diagonal menor:"))
    dma = float(input("ingrese diagonal mayor:"))
    a = (dma * dme) / 2

#fin_while
print("fin del bucle")
print("el area del rombo es:", a)
