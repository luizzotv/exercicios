from datetime import date
atual = date.today().year
ano = int(input('Digite o seu ano de nascimento, para saber a sua categoria de natação: '))
idade = atual - ano
print('O atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Sua categoria é: MIRIM.')
elif idade <=14:
    print('Sua categoria é: INFANTIL.')
elif idade <= 19:
    print('Sua categoria é: JUNIOR.')
elif idade <=20:
    print('Sua categoria é: SENIOR.')
else:
    print('Sua categoria é: MASTER.')
