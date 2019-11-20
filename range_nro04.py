#hallar la suma de los volumenes de una esfera que el radio comprende de 3 a 7
import os
pi=float(os.sys.argv[1])
volumen=0

#iterar el radio
for radio in range(3,8):
    print(radio)
    volumen=volumen+((4*pi*(radio**3))/3)

#fin_iterar
print("las suma de los volumenes de una esfera es:", volumen)
