#Condições Aninhasdas

nome = str(input('Qual é o seu nome? '))
if nome == 'Clauberto':
  print('Que nome diferente!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
  print('Seu nome é bem popular no Brasil')
elif nome == 'Ingrid':
  print('Olá Dig, que bom poder falar com você!')
else:
  print('Seu nome é bem normal no Brasil!')
print('Tenha um bom dia, {}!'.format(nome))
