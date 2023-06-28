# -*- coding: utf-8 -*-
"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 8 - Exercicio 5
Crie uma matriz de zeros de tamanho 10x10 e adicione uma borda de
valor 1.
"""

import numpy as np

matriz = np.zeros((10, 10), dtype=int)
print("Matriz original:")
print(matriz)

matriz[0, :] = 1  # Linha superior
matriz[-1, :] = 1  # Linha inferior
matriz[:, 0] = 1  # Coluna esquerda
matriz[:, -1] = 1  # Coluna direita

print("Matriz com borda de valor 1:")
print(matriz)