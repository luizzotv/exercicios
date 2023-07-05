velocidade = float(input('Qual a velocidade do seu carro? '))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print('Voce foi multado, o valor da multa é de R${:.2f}.'.format(multa))
else:
    print('Siga bem a sua viagem.')
