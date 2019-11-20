#hallar la suma de los volumenes de un prisma que su ancho comprende de 43 a 75
import os
largo=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
ancho=43

#iterar ancho
while (ancho<76):
    print(ancho)
    ancho+=1
    volumen=largo*ancho*altura

#fin_iterar
print("la suma de los volumenes de un prisma es:", volumen)
