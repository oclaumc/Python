'''leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo , calcule e mostre o compimento da hipotenusa.'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
