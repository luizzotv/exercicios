#s = 0
#acum = 0
#media = 0
#while True:
 #   v = int(input("Digite um numero a somar ou 0 para sair: "))
 #   if v == 0:
    #    break
   # s += v
    #acum += 1
   # media = s / acum
#print("Ao total voce digitou {} numeros e a soma total deles é de {} e sua media aritmética é de {}".format(acum, s, media)
compra = 0
while True:
    codigo = int(input('Digite o codigo do item, e digite 0 para calcular sua compra: '))
    quant = int(input('Qual a quantidade deste item:  '))
    if codigo == 1:
        compra = quant * 0.50
    elif codigo == 2:
        quant * 1.0
    elif codigo == 3:
        quant * 4.0
    elif codigo == 5:
        quant * 7.0
    elif codigo == 9:
        quant * 8.0
    elif codigo == 0:
        break
    else:
        print('CÓDIGO INVALIDO')
    print(compra)