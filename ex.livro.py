salario = float(input('digite o salario para calculo do imposto: '))
base = salario
imposto = 0
if base > 3000:
    imposto += ((base - 1000) * 0.35)
    base = 3000
if base > 1000:
    imposto += ((base - 1000) * 0.20)
print(f'salario: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}')
