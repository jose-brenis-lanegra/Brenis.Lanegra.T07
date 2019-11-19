#hallar el perimetro de un romboide si su base sea mayor igual a 99 o la altura menor a 98
base=float(input("ingrese base:"))
altura=float(input("ingrese altura:"))
p=2*base+2*altura

#mientras lo invalido
while (base<99 and altura>=98):
    base = float(input("ingrese base:"))
    altura = float(input("ingrese altura:"))
    p = 2 * base + 2 * altura

#fin_while
print("fin del bucle")
print("el perimetro de un romboide es:", p)
