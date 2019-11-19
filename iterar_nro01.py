#hallar la sumatoria de las areas de un hexagono cuando el apotema se comprende de 4 a 16
import os
base_h=float(os.sys.argv[1])
area=0

#iterar de 4 a 16
for apotema in range(4,17):
    area=area+(6*base_h*apotema)/2

#fin_iterar
print("el area del hexagono es:", area)
