vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('VOCE FUI MULTADO!')
    print('TERÁ QUE PAGAR UMA MULTA DE R${:.2f}'.format((vel-80)*7))
print('Tenha um bom dia, DIRIJA COM SEGRANÇA!')