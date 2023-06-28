# -*- coding: utf-8 -*-
"""
Guilherme AraÃºjo Mendes de Souza 
UNIFESP - ICT
AlgBio

Lista 8 - Exercicio 2
Crie um array unidimensional com valores aleatórios e inverta a
ordem dos elementos.
"""
import numpy as np

array = np.random.randint(1, 100, 5)
print("Array original:", array)

array_invertido = np.flip(array)
print("Array invertido:", array_invertido)
