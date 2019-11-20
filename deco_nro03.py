#decodificar un mensaje que contenga "f","+"y"<"
import os
mensaje=os.sys.argv[1]

#iterar mensaje
for simbolos in mensaje:
    if (simbolos=="f"):
        print("funcion")
    if (simbolos=="+"):
        print("mas")
    if (simbolos=="<"):
        print("mayor")
#fin_iterar

print("mensaje decodificado")
