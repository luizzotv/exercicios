from random import randint
from time import sleep
ne = randint (0, 5) #FAZ O COMPUTADOR PENSAR 
print('Vou pensar em um numero entre 0 e 5 tente adivinhar....')
num = int(input('Em que numero eu pensei? '))
print ('P R O C E S S A N D O . . . .')
sleep(2)
if num == ne:
    print('PARABENS, VOCE GANHOU!! EU PENSEI NO NUMERO {}'.format(ne))
else:
    print('EU GANHEI, EU PENSEI NO NUMERO {} TENTE NOVAMENTE...'.format(ne))
