'''Ler varios nomes, e exibi-los de forma aleatória'''
import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('terceiro nome:'))
n4 = str(input('terceito nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem de apresentação será ')
print(lista)
