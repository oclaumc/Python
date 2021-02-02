n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('Soma: {}\nProduto: {} \nDivisão: {:.3f}'.format(s, m, d), end=' ')
# :.3f formatação 3 casas decimais flutuantes
print('Divisão inteira: {} \nPotência {}'.format(di, e))
