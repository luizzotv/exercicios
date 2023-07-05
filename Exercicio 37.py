num = int(input('Digite um numero qualquer: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print ('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('\033[2;41m OPÇAO INVALIDA. TENTE NOVAMENTE\033[m')
