termo = int(input('digite o primeiro termo da PA:'))
razao = int(input('digite a razão da PA:'))
decimo = termo + 10 * razao
for c in range (termo, decimo, razao):
    print(c, end=' ~ ')
print('ACABOU!')
