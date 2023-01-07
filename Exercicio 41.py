ano = int(input('Digite o seu ano de nascimento, para saber a sua categoria de natação: '))
cat = 2023 - ano
if cat <= 9:
    print('Sua categoria é: MIRIM.')
elif cat <=14:
    print('Sua categoria é: INFANTIL.')
elif cat <= 19:
    print('Sua categoria é: JUNIOR.')
elif cat <=20:
    print('Sua categoria é: SENIOR.')
else:
    print('Sua categoria é: MASTER.')
    