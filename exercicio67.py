n = 0
while n > -1:
    n = int(input('De qual numero quer ver a tabuada: '))
    for c in range (1, 11):
        print(f'{n} x {c:2} = {n * c}')