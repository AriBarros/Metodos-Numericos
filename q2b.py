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

a = 121
b = 119
c = 0.327
exato = (a - b) - c
print(f'Cálculo exato: {exato}\n')

d = truncar(a - b, 3)
r = truncar(float(d) - c, 3)
print(f'Truncamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

d = truncar(a - b, 4)
r = truncar(float(d) - c, 4)
print(f'Truncamento com 4 dígitos: {r}')
calcularErros(exato, float(r))

d = arredondar(a - b, 3)
r = arredondar(float(d) - c, 3)
print(f'Arredondamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

d = arredondar(a - b, 4)
r = arredondar(float(d) - c, 4)
print(f'Arredondamento com 4 dígitos: {r}')
calcularErros(exato, float(r))
