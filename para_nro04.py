#hallar la suma de los volumenes de una esfera que el radio comprende de 3 a 7
import os
pi=float(os.sys.argv[1])
radio=3

#iterar el radio
while (radio<8):
    print(radio)
    radio+=1
    volumen=(4*pi*(radio**3))/3

#fin_iterar
print("las suma de los volumenes de una esfera es:", volumen)
