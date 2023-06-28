"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 10 - Exercicio 2
Escreva uma expressão que possa selecionar apenas os elementos de
índice par em um vetor, independente do tamanho do vetor. Teste essa
expressão em alguns vetores da sua escolha.
"""

import numpy as np

# Vetor de exemplo
vetor = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Selecionar os elementos de índice par
elementos_pares = vetor[::2]

print(elementos_pares)
