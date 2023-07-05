salario = float(input('Digite seu salario atual: '))
aumento = 0
if salario > 1250:
    aumento += (salario +(salario * 0.10))
print('seu salario com aumento de 10% passa a ser {}'.format(aumento))

if salario <= 1250:
    aumento += (salario + (salario * 0.15))
print('seu salario com aumento de 15% passa a ser {}.'.format(aumento))
