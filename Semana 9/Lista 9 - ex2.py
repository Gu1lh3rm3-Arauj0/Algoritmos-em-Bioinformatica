"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 9 - Exercicio 2
Utilizando NumPy, calcule a média, mediana, desvio padrão e
variância dos valores no array dados. Armazene cada resultado em
uma variável correspondente.
"""

import numpy as np

dados = np.random.randint(1, 101, 1000)

media = np.mean(dados)
mediana = np.median(dados)
desvio_padrao = np.std(dados)
variancia = np.var(dados)

print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)
print("Variância:", variancia)
