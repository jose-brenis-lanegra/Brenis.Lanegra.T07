#decodificar una contraseña que contenga ".","/"y"*"
import os
contrasena=os.sys.argv[1]

#iterar contraseña
for signos in contrasena:
    if (signos=="."):
        print("verde")
    if (signos=="/"):
        print("amarillo")
    if (signos=="*"):
        print("rojo")
#fin_iterar

print("contraseña decodificado")
