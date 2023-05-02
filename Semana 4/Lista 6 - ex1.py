"""
Semana 4 - Exercico 1
Escreva uma função chamada fatorial para calcular o
fatorial de um número inteiro.
"""

def f2(x):
    if x>1:
        return x*f2(x-1)
    else:
        return 1

a = int(input('Informe o valor: '))
print(f2(a))