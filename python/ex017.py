from math import sqrt, hypot

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#hi = sqrt(co ** 2 + ca ** 2)
hi = hypot(co, ca)
print(f'A hipotenuza vai medir {hi:.2f}.')
