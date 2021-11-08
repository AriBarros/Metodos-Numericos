import matplotlib.pyplot as plt
from decimal import *


def truncar(p, t):
    c = 0
    while(abs(p > 1)):
        p = p/10
        c = c+1
    if t == 1:
        p = Decimal(p).quantize(Decimal('0.1'), rounding=ROUND_DOWN)
    elif t == 2:
        p = Decimal(p).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    elif t == 3:
        p = Decimal(p).quantize(Decimal('0.001'), rounding=ROUND_DOWN)
    elif t == 4:
        p = Decimal(p).quantize(Decimal('0.0001'), rounding=ROUND_DOWN)
    elif t == 5:
        p = Decimal(p).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)
    elif t == 6:
        p = Decimal(p).quantize(Decimal('0.000001'), rounding=ROUND_DOWN)
    elif t == 7:
        p = Decimal(p).quantize(Decimal('0.0000001'), rounding=ROUND_DOWN)
    elif t == 8:
        p = Decimal(p).quantize(Decimal('0.00000001'), rounding=ROUND_DOWN)
    elif t == 9:
        p = Decimal(p).quantize(Decimal('0.000000001'), rounding=ROUND_DOWN)
    else:
        p = Decimal(p).quantize(Decimal('0.0000000001'), rounding=ROUND_DOWN)
    p = p*10**(c)
    return p


def calcularErroRelativo(p1, p2):
    return abs(p1 - p2) / abs(p1)
    

erroRelativoA = [0] * 10
erroRelativoB = [0] * 10
erroRelativoC = [0] * 10
erroRelativoD = [0] * 10
digitosTruncados = [i for i in range(1, 11)]
precisaoPadrao = [132.501, 1.673, 1.9535401391839955, -0.021496317541426446]

for i in range(10):
    erroRelativoA[i] = calcularErroRelativo(Decimal(precisaoPadrao[0]), truncar(precisaoPadrao[0], i+1))
    erroRelativoB[i] = calcularErroRelativo(Decimal(precisaoPadrao[1]), truncar(precisaoPadrao[1], i+1))
    erroRelativoC[i] = calcularErroRelativo(Decimal(precisaoPadrao[2]), truncar(precisaoPadrao[2], i+1))
    erroRelativoD[i] = calcularErroRelativo(Decimal(precisaoPadrao[3]), truncar(precisaoPadrao[3], i+1))

plt.plot(digitosTruncados, erroRelativoA, 'r')
plt.title('Item 2.a')
plt.xlabel('Dígitos truncados')
plt.ylabel('Erro relativo')
plt.show()
plt.plot(digitosTruncados, erroRelativoB, 'r')
plt.title('Item 2.b')
plt.xlabel('Dígitos truncados')
plt.ylabel('Erro relativo')
plt.show()
plt.plot(digitosTruncados, erroRelativoC, 'r')
plt.title('Item 2.c')
plt.xlabel('Dígitos truncados')
plt.ylabel('Erro relativo')
plt.show()
plt.plot(digitosTruncados, erroRelativoD, 'r')
plt.xlabel('Dígitos truncados')
plt.ylabel('Erro relativo')
plt.title('Item 2.d')
plt.show()
