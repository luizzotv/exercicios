l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses segmentos PODEM formar um triangulo ', end='')
    if l1 == l2 ==l3:
        print('EQUILATERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Esses segmentos NÃO FORMAM um triangulo')
