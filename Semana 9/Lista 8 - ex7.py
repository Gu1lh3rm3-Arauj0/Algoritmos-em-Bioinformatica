# -*- coding: utf-8 -*-
"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 8 - Exercicio 7
Crie um array unidimensional com valores aleatórios e encontre os
valores únicos e suas contagens.
"""

import numpy as np

array = np.random.randint(1, 10, 20) 
print("Array:", array)

# Encontrar os valores únicos e suas contagens
valores_unicos, contagens = np.unique(array, return_counts=True)

# Imprimir os valores únicos e suas contagens
for valor, contagem in zip(valores_unicos, contagens):
    print("Valor:", valor, "- Contagem:", contagem)
