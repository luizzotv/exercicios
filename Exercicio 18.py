from math import radians, sin, cos, tan
ang = float(input('digite um angulo:'))
seno = sin (radians(ang))
cos = cos (radians(ang))
tang = tan(radians(ang))
print ('o angulo {:.0f}°, tem o seno de {:.2f}, cosseno de {:.2f} e tangente {:.2f}.'.format(ang, seno, cos, tang))
