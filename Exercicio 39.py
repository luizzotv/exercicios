ano = int(input('Qual o seu ano de nascimento? '))
idade = 2023 - ano
print('Voce nasceu em {} e tem {} anos de idade.'.format(ano, idade))
if idade > 18:
    tempo = idade - 18
    print('Voce ja passou {} anos do periodo de alistamento militar.'.format(tempo))
elif idade == 18:
    print('Está na hora de voce se alistar ao serviço obrigatório militar.')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda não chegou sua hora de se alistar, e ainda faltam {} ano(s).'.format(tempo))
    