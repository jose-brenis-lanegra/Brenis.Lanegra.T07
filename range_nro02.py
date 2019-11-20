#hallar la suma de las areas de un circulo que su radio comprende de 1 a 8
import os
pi=float(os.sys.argv[1])
area=0

#iterar el radio
for radio in range(1,9):
    print(radio)
    area=area+pi*(radio**2)

#fin_iterar
print("la suma de las areas del circulo es:", area)
