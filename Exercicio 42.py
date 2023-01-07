l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))
if l1 > l2 + l3 and l2 > l1 + l3 and l3 > l1 + l2:
    print('Esses segmentos NÃO podem formar um triangulo .')

else:
    eq = l1 == l2 == l3
    print('Esses segmentos FORMAM um triangulo')
   
print('Esses segmentos formam um triangulo{}'.format(eq))