"""
Guilherme Araújo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 6 - Exercicio 3
Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
"""

def verifica (a, b):
    if a % b == 0:
        return True
    else:
        return False

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(verifica(num1, num2))