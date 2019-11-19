#hallar la suma de los volumenes de un prisma que su ancho comprende de 43 a 75
import os
largo=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
volumen=0

#iterar ancho
for ancho in range(43,76):
    volumen=volumen+largo*ancho*altura
    
#fin_iterar
print("la suma de los volumenes de un prisma es:", volumen)
