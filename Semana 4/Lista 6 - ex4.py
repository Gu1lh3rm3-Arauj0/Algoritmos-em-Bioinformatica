"""
Guilherme Araújo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 6 - Exercicio 4
Crie uma função na qual calcula o valor do seno a partir da série de Taylor (50 primeiros termos) e cosseno a partir da seguinte identidade a baixo. Obs: Fazer a serie utilizando for e utilizar a função fatorial desenvolvida no exercício 1.
"""

def fatorial(x):
    if x>1:
        return x*fatorial(x-1)
    else:
        return 1

def seno(x):
    sen = x
    
    for i in range (3, 25, 4):
        sen = sen - ((x**i)/fatorial(i))
    
    for i in range (5, 25, 4):
        sen = sen + ((x**i)/fatorial(i))

    return sen

def cosseno(x):
    y = 1 - x**2
    cos = y** (1/2)
    
    return cos

a = float(input('Informe o valor de X: '))
b = seno(a)
c = cosseno(b)

print(f'O Seno de {a} é {b} e o Cosseno de {a} é {c}')