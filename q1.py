def calcularErros(p1, p2):
    erro_absoluto = abs(p1 - p2)
    erro_relativo = abs(p1 - p2) / abs(p1)
    print('Erro absoluto: ', erro_absoluto)
    print('Erro relativo: ', erro_relativo, '\n')

def fatorial(n):
    if n == 1:
        return 1
    return n*fatorial(n-1)

pi = 3.14159265359
e = 2.71828182846

#Item (a)
p = 10**pi
p_asterisco = 1400
calcularErros(p, p_asterisco)

#Item (b)
p = 2**(1/2)
p_asterisco = 1.414
calcularErros(p, p_asterisco)

#Item (c)
p = e**10
p_asterisco = 22000
calcularErros(p, p_asterisco)

#Item (d)
p = fatorial(8)
p_asterisco = 39900
calcularErros(p, p_asterisco)
