#hallar la suma de las areas de un circulo que su radio comprende de 1 a 8
import os
pi=float(os.sys.argv[1])
radio=1

#iterar el radio
while (radio<9):
    print(radio)
    radio+=1
    area=pi*(radio**2)

#fin_iterar
print("la suma de las areas de un circulo es:", area)
