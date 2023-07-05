km = float(input('Digite a distancia que deseja percorrer em km: '))
passagem = 0
if km <= 200:
    passagem += (km * 0.50)
else:
    passagem += (km * 0.45)
print('O valor da sua passagem será de R${:.2f}.'.format(passagem))