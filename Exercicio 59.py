from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
maior = v1
escolha = 0

while escolha != 5:
    print(' [1]somar\n [2]multiplicar\n [3]maior\n [4]novos numeros\n [5]sair do programa\n ')
    escolha = int(input('Digite sua opção: '))
    if escolha == 1:
        soma = v1 + v2
        print('A soma entre {} + {} = {}'.format(v1, v2, soma))
        
    elif escolha == 2:
        produto = v1 * v2
        print('A multiplicação entre {} x {} = {}'.format(v1, v2, produto))
        
    elif escolha == 3:
        maior = v1
        if v2 > maior:
            maior = v2
            print('O maior valor entre {} e {} é {}'.format(v1, v2, v2))
        elif maior > v2:
            print('O maior valor entre {} e {} é {}'.format(v1, v2, v1))
        else:
            print('Não existem maiores, eles são IGUAIS.')
        
    elif escolha == 4:
        print('Digite os novos valores.')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
        
    elif escolha == 5:
        print('> > > F I N A L I Z A N D O < < <')
        sleep(3)

    else:
        print('OPÇÃO, INVÁLIDA!! Tente novamente digitando uma opção válida.')
    print('=~='*10)
print('THE END. ALWAYS COME BACK.')
        