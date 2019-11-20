#calcular el producto de areas totales de un cilindro cuando su altura comprende de 1 a 13
import os 
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
area=1

#iterar la altura
for altura in range(1,13):
    area=area*2*pi*radio*(radio + altura)
    
#fin_iterar
print("el producto de las areas totales de un cilindro es:", area)
