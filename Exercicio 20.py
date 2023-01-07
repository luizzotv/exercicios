import random
n1 = str(input('digite os quatro integrantes do grupo, primeiro:'))
n2 = str(input('segundo:'))
n3 = str(input('terceiro:'))
n4 = str(input('terceiro:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print ('a ordem de quem ira apresentar o trabalho sera: {}'.format(lista))
