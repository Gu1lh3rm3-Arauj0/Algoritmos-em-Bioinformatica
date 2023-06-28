"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 9 - Exercicio 3
Crie um histograma com 20 bins utilizando a função plt.hist() para
visualizar a distribuição dos valores no array dados.
"""

import numpy as np
import matplotlib.pyplot as plt

dados = np.random.randint(1, 101, 1000)

plt.hist(dados, bins=20)
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma dos Valores')
plt.show()
