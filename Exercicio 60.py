#dias = int(input('Quantos dias: '))
#horas = float(input('Quantas horas: '))
#min = int(input('quantos minutos: '))
#seg = float(input('quantos segundos: '))
#somadias = dias * 86400
#somahoras = horas * 3600
#somamin = min * 60
#print(f'a soma de {dias} dias {horas} horas, {min} min e {seg} segundos, somados todos em segundos é de: {somadias + somahoras + somamin + seg}s')###



quantcigarros = int(input('Quantos cigarros voce fuma por dia? '))
anosfumado = int(input('Por quantos anos voce ja fumou? '))
perca = quantcigarros * 365 * anosfumado
calculovida = perca / 144
print(f'Se voce fumar {quantcigarros} cigarros por dia durante {anosfumado} anos voce perderá {calculovida:2f} dias de vida')
