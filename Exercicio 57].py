sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção invalida, informe seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso.'.format(sexo))