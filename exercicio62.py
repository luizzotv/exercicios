print('Gerador de PA')
print ('=~=' * 10)

primeiro = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end ='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('Progressão finalizada com {} termos.'.format(total))
print('F I M !')
