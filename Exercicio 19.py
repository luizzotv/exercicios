from random import choice
n1 = input('digite um nome:')
n2 = input('outro nome:')
n3 = input('mais um nome:')
n4 = input('mais um nome:')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print ('o nome escolhido foi {}'.format(escolhido))

