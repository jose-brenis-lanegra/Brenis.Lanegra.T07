#hallar la sumatoria de las areas de un hexagono cuando el apotema se comprende de 4 a 16
import os
base_h=float(os.sys.argv[1])
apotema=4

#iterar la apotema
while (apotema<17):
    print(apotema)
    apotema+=1

#processing
area=(6*base_h*apotema)/2

#fin_while
print("la suma de las areas del hexagono es:", area)
