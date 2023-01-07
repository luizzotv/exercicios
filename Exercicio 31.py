viagem = float (input('qual a distancia da sua viagem? '))
print('voce esta prestes a comecar uma viagem de {}km.'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
    #print('Sua passagem custará R${:.2f}'.format( viagem * 0.5))
else:
    preço = viagem * 0.45
    #print('Sua viagem custará R${:.2f}'.format( viagem * 0.45))
print('Sua passagem custará R${:.2f}'.format(preço))



#preço=viagem * 0.50 if viagem <= 200 else viagem * 0.45