s = float(input('\033[0;32m Qual o seu salário atual? R$\033[m'))
if s > 1250.00:
    print('\033[0;37mSeu salário terá um aumento de 10% e passará a ser de R${:.2f} . \033[m'.format((s * 10 /100) + s))
   
else:
    print('\033[1;44mSeu salário terá um aumento de 15% e passará a ser de {:.2f}\033[m'.format((s * 15 /100) + s))
    
    
