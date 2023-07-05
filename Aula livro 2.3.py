consumo = float(input('Qual a quantidade de kWh consumida: '))
tipo = int(input('Qual o tipo de instalação? [ 1 ] RESIDENCIAL, [ 2 ] COMERCIAL, [ 3 ] INDUSTRIAL: '))
preço = 0
if tipo == 1:
    if consumo <= 500:
        preço = 0.40
        print('Sua conta do tipo RESIDENCIAL ficou no valor de: R${:.2f}'.format(preço * consumo))
    elif consumo > 500:
        preço = 0.65
        print('Sua conta do tipo RESIDENCIAL ficou no valor de R${:.2f}'.format(preço * consumo))
elif tipo == 2:
    if consumo <= 1000:
        preço = 0.55
        print('Sua conta do tipo COMERCIAL ficou no valor de {:.2f}'.format(preço * consumo))
    elif consumo > 1000:
        preço = 0.60
        print('Sua conta do tipo COMERCIAL ficou no valor de R${:.2f}'.format(preço * consumo))
elif tipo == 3:
    if consumo <= 5000:
        preço = 0.55
        print('A sua conta do tipo INDUSTRIAL ficou no valor de R${:.2f}'.format(preço * consumo))
    elif consumo > 5000:
        preço = 0.60
        print('A sua conta do tipo INDUSTRIAL ficou no valor de R${:.2f}'.format(preço * consumo))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE INSERINDO UMA DAS OPÇOES VALIDAS!')
    