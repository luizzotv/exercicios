preço = float(input('qual o preço do produto: R$'))
vista = preço - (preço*5/100)
p1 =  (preço + (preço*2/100))/2
p2 =  (preço + (preço*3/100))/3
p3 =  (preço + (preço*4/100))/4
p4 =  (preço + (preço*5/100))/5
print ('O produto que custa R${:.2f}, a vista tera um desconto de 5% e passrá a custar R${:.2f}. \n Ver parcelas disponiveis:  \n 2 X de: R${:.2f} + 2%de juros. \n 3 X de: R${:.2f} + 3% de juros. '.format(preço, vista, p1, p2))
