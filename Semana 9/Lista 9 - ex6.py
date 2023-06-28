"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 9 - Exercicio 6
Imprima na tela as estatísticas resumidas dos valores no array
dados_filtrados utilizando a função np.stats.describe().
"""
import numpy as np

dados = np.random.randint(1, 101, 1000)
media = np.mean(dados)
dados_filtrados = dados[dados > media]

estatisticas = {
    'mínimo': np.min(dados_filtrados),
    'máximo': np.max(dados_filtrados),
    'soma': np.sum(dados_filtrados),
    'média': np.mean(dados_filtrados),
    'mediana': np.median(dados_filtrados),
    'desvio padrão': np.std(dados_filtrados),
    'variância': np.var(dados_filtrados)
}

print(estatisticas)

