deposito = float(input('Deposito inicial: R$'))
taxa = float(input('Taxa de juros da poupança: '))
juros = deposito * taxa / 100
mes = 1
valor = deposito
while mes <= 24:
    print('Mes {} valor R${:.2f}'.format(mes, valor + juros))
    mes = mes + 1
    valor = valor + deposito * juros  



    a=4
    b=10
    c=5.0
    d=1
    f=5   