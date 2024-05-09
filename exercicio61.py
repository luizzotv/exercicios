print('Gerador de PA')
print ('=~=' * 10)

primeiro = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1

print('F I M.')
