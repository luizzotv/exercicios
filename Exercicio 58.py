from random import randint
from time import sleep
ne = randint (0,10)
print('Vou pensar em um numero de 0 a 10, tente adivinhar!')
num = int(input('Em que numero eu pensei: '))
print(' P R O C E S S A N D O . . .')
sleep (1)
tentativa = 1
while num != ne:
    num = int(input('Voce PERDEU, eu pensei em outro numero TENTE NOVAMENTE: '))
    if num != ne:
        tentativa += 1
print('PARABENS, VOCE VENCEU! EU PENSEI NO NUMERO {} e voce levou {} tentativas para acertar.'.format(ne, tentativa))
