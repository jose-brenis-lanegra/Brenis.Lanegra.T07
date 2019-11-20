#calcular la suma de areas totales de un cilindro cuando su altura comprende de 1 a 13
import os
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
altura=1

#iterar la altura
while (altura<14):
    print(altura)
    altura+=1
    area=2*pi*radio*(radio + altura)

#fin_iterar
print("la suma de las areas totales de un cilindro es:", area)
