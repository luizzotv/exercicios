soma = 0
cont = 0 
for c in range (1, 500, 2):
    if c % 3 == 0:
        cont += 1 
        soma = soma + c
print (' a soma de todos os {} valores solicitados é de {}'.format(cont, soma))   
     