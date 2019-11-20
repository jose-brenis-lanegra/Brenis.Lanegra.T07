#hallar la suma de las areas de un circulo que su radio comprende de 1 a 8
import os
pi=float(os.sys.argv[1])
radio=1

#iterar el radio
while (radio<9):
    print(radio)
    radio+=1

#processing
area=pi*(radio**2)

#fin_iterar
print("el poducto de las areas del circulo es:", area)
