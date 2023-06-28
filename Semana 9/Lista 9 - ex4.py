"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 9 - Exercicio 4
Crie um novo array chamado dados_filtrados que contenha apenas
os valores maiores que a média calculada no passo 3.
"""

import numpy as np

dados = np.random.randint(1, 101, 1000)

media = np.mean(dados)

dados_filtrados = dados[dados > media]

print(dados_filtrados)
