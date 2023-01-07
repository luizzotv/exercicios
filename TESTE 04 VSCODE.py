nome = str(input('Qual é o seu nome: '))
if nome == 'Luiz':
    print('Seu nome é diferenciado, PARABENS!!')
elif nome == 'Antonella':
    print('O seu nome é o mais lindo do mundo, pois, é o nome da minha filha.')
elif nome == 'Luiza' or nome == 'Dione':
    print('O seu nome, é o mesmo de uma mulher MAGNIFICA em minha vida.')
else:
    print('Apesar de seu nome ser  normal, é bem conhecido no Brasil.')
print('Tenha um bom dia, {}!!'.format(nome))    
