soma = 0
cont = 0
for c in range (0, 6):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        cont += 1
        soma += n
print ('A soma de {} valores pares é de {}'.format(cont, soma))
