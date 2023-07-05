
def jogar0():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input('Qual a letra? ')
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
               letras_acertadas [index] = letra 
            index = index + 1

        print(letras_acertadas)

    print('*******************************')
    print('FIM DE JOGO!')
    print('*******************************')
if __name__ == "__main__":
    jogar0()

numeros = [10, 20, 30, 40, 50]

