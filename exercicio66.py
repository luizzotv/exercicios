n = quant = s = 0
while True:
    n = int(input('Digite um numero (999 para sair): '))
    if n == 999:
        break
    quant += 1
    s += n
print(f'A soma de {quant} valores é igual a {s}.')
