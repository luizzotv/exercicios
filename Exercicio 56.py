somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1,5):
    print ('{}ª PESSOA'.format(p))
    nome = str(input('NOME: '))
    idade =(int(input('IDADE: ')))
    sexo = (input('SEXO [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff'and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print('A média da idade do grupo foi de: {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo tem {} mulheres com menos de 20 anos de idade'.format(totmulher20))
