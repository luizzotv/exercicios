print ('{:\^40}'.format('LOJA DO SEU LUIZ'))
preço = float(input('Qual o preço das compras:R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total =  (preço - (preço * 10 / 100))
elif opção == 2:
     total = (preço - (preço * 5 / 100))
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Sua compra vai ser parecelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print ('Sua compra vai ser parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('Opçãp de pagamento INVALIDA. TENTE NOVAMENTE')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
