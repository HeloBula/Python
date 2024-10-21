
#Resolvendo equações de segundo grau com python. Utilizando a fórmula de Bhaskara
import math

a = 9
b = -24
c = 16

delta = pow(b,2) - (4*a*c)

if(delta<0):
    print("Delta Ngeativo, não pode resolver")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

    print("As duas soluções possívei são x1:", x1 , ", e x2:" , x2)