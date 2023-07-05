casa = float(input('Qual o valor da casa que voce quer comprar? R$'))
salario = float(input('Qual é o seu salário atual? R$'))
anos = int(input('Em quantos anos deseja pagar o imovel? '))
parcela = casa / (anos * 12)
if parcela > salario * 0.30:
    print('Emprestimo negado, as parcelas irao superar 30% do seu salário.')
elif parcela <= salario * 0.30:
    print('Emprestimo aprovado, seu financiamento ficara com {} parcelas de R${:.2f}'.format(anos * 12, parcela)) 
