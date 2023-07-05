from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print ('JO')
sleep (1)
print ('KEN')
sleep (1)
print ('PO')
sleep (1)
print ('>' *20)
print ('O jogador jogou {}'.format(itens[jogador]))
print ('O computador jogou {}'.format(itens[cpu]))
print('<' *20)
if cpu == 0:
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print ('JOGADOR VENCEU')
    elif jogador == 2:
        print ('CPU VENCEU')
    else: 
        print('JOGADA INVALIDA')    
elif cpu == 1:
    if jogador == 0:
        print ('JOGADOR VENCE')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print ('CPU VENCEU')
    else:
        print ('jogada INVALIDA')            
elif cpu == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('CPU VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print ('JOGADA INVALIDA')
