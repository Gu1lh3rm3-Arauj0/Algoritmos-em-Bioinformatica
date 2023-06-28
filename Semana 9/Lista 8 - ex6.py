# -*- coding: utf-8 -*-
"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 8 - Exercicio 6
Crie um array unidimensional com valores aleatórios e encontre o
índice do valor mais próximo de um valor fornecido
"""

import numpy as np

array = np.random.random(10)
print("Array:", array)

# Valor fornecido
valor_fornecido = float(input('informe o valor: '))

# Encontrar o índice do valor mais próximo
indice_valor_proximo = np.abs(array - valor_fornecido).argmin()

print("Índice do valor mais próximo:", indice_valor_proximo)
print("Valor mais próximo:", array[indice_valor_proximo])