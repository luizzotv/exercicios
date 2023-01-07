from math import hypot
co = float(input('quanto mede o cateto oposto: '))
ca = float(input('quanto mede o cateto adjacente: '))
hy = hypot(co, ca)
print('A hipotenusa desse triangulo retangulo vale {:.2f}.'.format(hy))
