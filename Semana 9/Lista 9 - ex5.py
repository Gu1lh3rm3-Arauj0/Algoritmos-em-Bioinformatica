"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 9 - Exercicio 4
Utilizando a função plt.boxplot(), crie um boxplot para visualizar a
distribuição dos valores no array dados_filtrados.
"""

import numpy as np
import matplotlib.pyplot as plt

dados = np.random.randint(1, 101, 1000)
media = np.mean(dados)
dados_filtrados = dados[dados > media]

plt.boxplot(dados_filtrados)
plt.xlabel('Dados Filtrados')
plt.ylabel('Valores')
plt.title('Boxplot dos Dados Filtrados')
plt.show()
