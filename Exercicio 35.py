l1 = float (input ('Primeiro segmento: '))
l2 = float (input ('Segundo segmento:'))
l3 = float ( input('Terceiro segmento: '))
if l1 > l2 + l3 and l2 > l1 + l3 or l3 > l1 + l2:
#l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l3: PODE FORMAR TRIANGULO!!
    print('\033[1;30;41m Não pode formar um triangulo!!!\033[m')
else:
    print('\033[1;30;44mPode formar um triangulo!!!\033[m')