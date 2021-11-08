from decimal import *

def truncar(p, t):

    c = 0
    while(abs(p > 1)):
        p = p/10
        c = c+1
    if t == 3:
        p = Decimal(p).quantize(Decimal('0.001'), rounding=ROUND_DOWN)
    else:
        p = Decimal(p).quantize(Decimal('0.0001'), rounding=ROUND_DOWN)
    p = p*10**(c)
    
    return p
    

def arredondar(p, a):

    c = 0
    while(abs(p > 1)):
        p = p/10
        c = c+1
    if a == 3:
        p = Decimal(p).quantize(Decimal('0.001'), rounding=ROUND_HALF_DOWN)
    else:
        p = Decimal(p).quantize(Decimal('0.0001'), rounding=ROUND_HALF_DOWN)
    p = p*10**(c)
    
    return p
    

def calcularErros(p1, p2):
    erro_absoluto = abs(p1 - p2)
    erro_relativo = abs(p1 - p2) / abs(p1)
    print('Erro absoluto: ', erro_absoluto)
    print('Erro relativo: ', erro_relativo, '\n')

a = 13
b = 14
c = 6
d = 7
e = 2.71828182846
f = 5.4

exato = ((a/b) - (c/d))/(2*e - 5.4)
print(f'Cálculo exato: {exato}\n')

m = truncar(a / b, 3)
n = truncar(c / d, 3)
o = truncar(m - n, 3)
p = truncar(2 * e, 3)
q = truncar(float(p) - f, 3)
r = truncar(o / q, 3)
print(f'Truncamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

m = truncar(a / b, 4)
n = truncar(c / d, 4)
o = truncar(m - n, 4)
p = truncar(2 * e, 4)
q = truncar(float(p) - f, 4)
r = truncar(o / q, 4)
print(f'Truncamento com 4 dígitos: {r}')
calcularErros(exato, float(r))

m = arredondar(a / b, 3)
n = arredondar(c / d, 3)
o = arredondar(m - n, 3)
p = arredondar(2 * e, 3)
q = arredondar(float(p) - f, 3)
r = arredondar(o / q, 3)
print(f'Arredondamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

m = arredondar(a / b, 4)
n = arredondar(c / d, 4)
o = arredondar(m - n, 4)
p = arredondar(2 * e, 4)
q = arredondar(float(p) - f, 4)
r = arredondar(o / q, 4)
print(f'Arredondamento com 4 dígitos: {r}')
calcularErros(exato, float(r))
