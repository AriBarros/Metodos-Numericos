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

pi = 3.14159265359
a = 22
b = 7
c = 1
d = 17

exato = (pi - (a/b)) / (c / d)
print(f'Cálculo exato: {exato}\n')

o = truncar(a / b, 3)
p = truncar(pi - float(o), 3)
q = truncar(c / d, 3)
r = truncar(p / q, 3)
print(f'Truncamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

o = truncar(a / b, 4)
p = truncar(pi - float(o), 4)
q = truncar(c / d, 4)
r = truncar(p / q, 4)
print(f'Truncamento com 4 dígitos: {r}')
calcularErros(exato, float(r))

o = arredondar(a / b, 3)
p = arredondar(pi - float(o), 3)
q = arredondar(c / d, 3)
r = arredondar(p / q, 3)
print(f'Arredondamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

o = arredondar(a / b, 4)
p = arredondar(pi - float(o), 4)
q = arredondar(c / d, 4)
r = arredondar(p / q, 4)
print(f'Arredondamento com 4 dígitos: {r}')
calcularErros(exato, float(r))
