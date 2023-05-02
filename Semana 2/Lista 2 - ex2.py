"""
Exercicio 2 - Semana 2
"""
resp = input('Continuar(s/n)?')
f = resp = 'n' or 'N'

if resp == 's' or 'S':
    print('OK, continuar')
elif resp == 'n' or 'N':
    print('OK, parar')
else:
    print('ERRO')