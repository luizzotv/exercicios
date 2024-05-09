numeros = ('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze', 'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')


selecionado = int(input('Digite um numero entre 0 e 20:'))

for selecionado in range(0, len(numeros)):
    print(f'voce esolheu o numero{numeros}')