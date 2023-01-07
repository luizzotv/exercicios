dias = int(input('quantos dias o carro ficou alugado?'))
km = float(input('quantos km rodados?'))
diaria = (dias*60) + (km*0.15)
print ('o valor a ser pago é de {:.2f}'.format(diaria))
