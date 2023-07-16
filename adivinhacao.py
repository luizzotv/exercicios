import random as gerar
###from random import randint

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = gerar.randrange(1, 101)
    ###numero_secreto = randint(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print ('Qual o nível de dificuldade voce deseja? \n [1] Fácil \n [2] Médio \n [3] Difícil')
    nível = int(input('Digite o nível escohido: '))

    if nível == 1:
        total_de_tentativas = 20
    elif nível == 2:
        total_de_tentativas = 10
    elif nível == 3:
        total_de_tentativas = 5 

    for rodada in range (1, total_de_tentativas + 1):
        print('tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print('OPÇÃO INVÁLIDA, voce deve digitar um numero entre 1 e 100!')
            continue

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print('ERROU, voce digitou um numero MAIOR que o numero secreto!')
            elif (menor):
                print('ERROU, voce digitou um numero MENOR que o numero secreto!')
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos -= pontos_perdidos

        print('*******************************')
        print('FIM DE JOGO!')
        print('*******************************')

if __name__ == "__main__":
    jogar()
