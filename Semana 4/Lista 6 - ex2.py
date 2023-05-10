"""
Guilherme Araújo Mendes de Souza
UNIFESP - ICT
alg bio

Exercicio 2 - Lista 6
Escreva uma função chamada maxnum que retorne o maior número de um conjunto de números. Utilize empacotamento para fazer a função.
"""

def maxnum (*a):
    return max(a)
    
lista = []

for i in range (5):
    lista.append(int(input('Informe um número: ')))
print(f'O valor máximo é {maxnum(*lista)}')