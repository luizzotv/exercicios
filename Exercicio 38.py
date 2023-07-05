n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor:'))
if n1 > n2:
    print('O  1º numero {} é maior que o 2º numero {}'.format(n1, n2))
elif n2 > n1:
    print('O 2º numero {} é maior que o 1º numero {}'.format(n2, n1))
else:
    print('NÃO exite um numero maior, neste caso os dois são IGUAIS.')
