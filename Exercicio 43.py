peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / altura ** 2
print ('Seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print ('PARABENS, voce está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('PRESTE ATENÇÃO voce esta com SOBREPESO.')
elif imc > 30 and imc <= 40:
    print('CUIDADO, voce está OBESO(A).')
elif imc > 40:
    print('PROCURE JA, a ajuda de um profissional, pois voce está com OBESIDADE MÓRBIDA!!!')
    