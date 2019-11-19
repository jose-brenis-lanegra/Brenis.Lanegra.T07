#hallar el perimetro y area de un cuadrado cuyo lado sea diferente de 100
import os
lado=float(os.sys.argv[1])
p=4*lado
a=lado**2

#mientras lo que invalida
while (lado==100):
    lado = float(input("ingrese el lado:"))
    p = 4 * lado
    a = lado ** 2
    
#fin_while
print("fin del bucle")
print("el perimetro del cuadrado es:", p)
print("el area del cuadrado es:", a)
