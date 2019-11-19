#hallar el producto de las areas de un circulo que su radio comprende de 1 a 8
import os
pi=float(os.sys.argv[1])
area=1

#iterar el radio
for radio in range(1,9):
    area=area*pi*(radio**2)

#fin_iterar
print("el poducto de las areas del circulo es:", area)
