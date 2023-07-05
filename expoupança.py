valor = float(input('Qual valor que será depositado? R$'))
deposito = 0
taxa_de_juros = float(input('Qual a taxa de juros desejada: '))
juros = valor / 100 * taxa_de_juros

for c in range (1, 25):
    print('Mes {}, valor R${:.2f}'.format(c, valor + juros))
    juros += juros