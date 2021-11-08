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

a = 133
b = 0.499
exato = a - b
print(f'Cálculo exato: {exato}\n')

r = truncar(a - b, 3)
print(f'Truncamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

r = truncar(a - b, 4)
print(f'Truncamento com 4 dígitos: {r}')
calcularErros(exato, float(r))

r = arredondar(a - b, 3)
print(f'Arredondamento com 3 dígitos: {r}')
calcularErros(exato, float(r))

r = arredondar(a - b, 4)
print(f'Arredondamento com 4 dígitos: {r}')
calcularErros(exato, float(r))
