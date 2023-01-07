n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('\033[4;41mEstude MAIS, voce está REPROVADO.\033[m')
elif m == 5.0 or m <= 6.9:
    print('\033[0;32;43mQue pena, voce está de RECUPERAÇÃO\033[m')
elif m > 6.9:
    print('\033[1;44mParabens, voce está APROVADO!\033[m')
    