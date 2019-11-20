#decodificado una clave que contenga "x","t"y"g"
import os
clave=os.sys.argv[1]

#iterar clave
for codigos in clave:
    if (codigos=="x"):
        print("seguido")
    if (codigos=="t"):
        print("separado")
    if (codigos=="g"):
        print("junto")
#fin_iterar

print("clave decodificado")
