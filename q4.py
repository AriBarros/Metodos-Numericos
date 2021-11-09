from decimal import *


def arredondar(p):
    c = 0
    while(abs(p > 1)):
        p = p/10
        c = c+1
    p = Decimal(p).quantize(Decimal('0.001'), rounding=ROUND_HALF_DOWN)
    p = p*10**(c)
    return p  

def calcularErroRelativo(p1, p2):
    return abs(p1 - p2) / abs(p1)


x0 = 1.31
y0 = 3.24
x1 = 1.93
y1 = 4.76

xExato = (x0*y1 - x1*y0) / (y1 - y0)

a = arredondar(x0 * y1)
b = arredondar(x1 * y0)
c = arredondar(a - b)
d = arredondar(y1 - y0)
r1 = arredondar(c / d)

e = arredondar(x1 - x0)
f = arredondar(float(e) * y0)
g = arredondar(y1 - y0)
h = arredondar(f / g)
r2 = arredondar(x0 - float(h))

print(f'\nResultado exato: {xExato}')
print(f'\nResultado da fórmula 1: {r1}')
print('Erro relativo:', calcularErroRelativo(xExato, float(r1)))
print(f'\nResultado da fórmula 2: {r2}')
print('Erro relativo:', calcularErroRelativo(xExato, float(r2)))

if(calcularErroRelativo(xExato, float(r1)) <
            calcularErroRelativo(xExato, float(r2))):
    print('\nA primeira fórmula funciona melhor com o arredondamento ', end="")
    print('com 3 dígitos, porque tem menor erro relativo ao resultado exato.')
else:
    print('\nA segunda fórmula funciona melhor com o arredondamento ', end="")
    print('com 3 dígitos, porque tem menor erro relativo ao resultado exato.')
