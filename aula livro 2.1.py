n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
escolha = int(input('[ 1 ] soma [ 2 ] subtração [ 3 ] multiplicação [ 4 ] divisão. Digite a operação que dejesa realizar: '))
if escolha == 1:
    print (n1 + n2)
elif escolha == 2:
    print (n1 - n2)
elif escolha == 3:
    print (n1 * n2)
elif escolha == 4:
    print (n1 / n2)
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE ESCOLHENDO UMA DAS OPÇÕES VÁLIDAS.')
