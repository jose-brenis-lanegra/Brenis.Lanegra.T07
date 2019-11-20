#decodificar una cadena que contenga "j","4"y"d"
import os
cadena=os.sys.argv[1]

#iterar cadena
for letras in cadena:
    if (letras=="j"):
        print("joven")
    if (letras=="4"):
        print("bebe")
    if (letras=="d"):
        print("anciano")
#fin_iterar

print("cadena decodificada")
