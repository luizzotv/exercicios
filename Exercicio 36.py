print ('{:=^40}'.format('ANTONELLA CENTER BANK'))
preço = float (input('Qual o preço da casa? R$'))
salário = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos voce deseja parcelar a sua casa? '))
parc = anos * 12
parcela = preço / parc
if parcela > salário *30 / 100:
    print('''   OPS...
    INFELIZMENTE A SUA PARCELA EXCEDE 30% DE SUA RENDA
    POR ESSE MOTIVO, O SEU EMPRÉSTIMO SERÁ  NEGADO.''')
elif parcela < salário * 30 / 100:
    print('PARABÉNS, SEU EMPRÉSTIMO CONSIGNADO FOI APROVADO!!')
print('A seu financiamento da casa própria ficará em {}x de R${:.2f}'.format(parc, parcela))
