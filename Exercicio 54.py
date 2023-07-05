from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    nasc = int(input('em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('''Ao todo tivemos {} pessoas MAIORES de idade
    e tambem tivemos {} pessoas MENORES de idade.'''.format(maior, menor))
    