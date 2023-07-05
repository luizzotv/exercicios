#velocidade = int(input('Qual a velocidade do carro? '))
#multa = (velocidade - 80) * 5
#if velocidade <= 80:
 #   print('Voce esta dentro da velocidade')
#if velocidade > 80:
  #  print('Voce ultrapassou o limite de velocidade e sera multado em R${:.2f}.'.format(multa))




# salario = float (input('Digite seu salario para calculo de imposto:'))
# base = salario
# imposto = 0
# if base > 3000:
#     imposto = imposto + ((base - 3000) * 0.35)
#     base = 3000
# if base > 1000:
#     imposto  = imposto + ((base - 1000) * 0.20)
# print(f'Salario: R$ {salario:6.2f} Imposto a pagar: R${imposto:6.2f}')


deposito = float(input("deposito"))
taxa = float(input("taxa de juros"))
valor_total = deposito
# juros_total = 0.0

for x in range(24):
    renda = valor_total * (taxa/100)
    print(f"valor que rendeu no mes {x+1} : {renda}")
    valor_total = valor_total + renda
    if x == 4:
        break



print(deposito)
print(valor_total)
print(valor_total-deposito)
