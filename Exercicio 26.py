frase = str(input('Digite uma frase:')).strip() . lower()
print ('\033[4;36mA letra A apareceu {} vezes na frase.\033[m'.format(frase.count('a')))
print('\033[0;33mA primeira letra A apareceu na posição {}\033[m'.format(frase.find('a') + 1 ))
print ('\033[0;32mA ultima letra A apareceu na posição {}\033[m '.format(frase.rfind('a') + 1 ))

