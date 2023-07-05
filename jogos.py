import adivinhacao
import forca

print('*******************************')
print('ESCOLHA SEU JOGO!')
print('*******************************')

jogo = int(input('[1] Adivinhação [2] Forca \n Qual jogo voce deseja jogar? '))

if jogo == 1:
    print('Jogando Adivinhação!')
    adivinhacao.jogar()
elif jogo == 2:
    print('Jogando Forca!')
    forca.jogar()
