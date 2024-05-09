soma = c = n = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} termos e a soma é igual a {}'.format(c, soma))
