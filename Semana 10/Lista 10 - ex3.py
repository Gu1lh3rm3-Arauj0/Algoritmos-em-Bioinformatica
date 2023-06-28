"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 10 - Exercicio 3
Crie uma matriz 4 x 3 de números aleatórios inteiros no intervalo -5 a 5 e
armazene em uma variável “mat”.
a. Escreva um comando que retorna o valor absoluto dos elementos
dessa matriz.
b. Escreva um comando que retorna o seno dos valores contidos na
primeira linha dessa matriz.
c. Escreva um comando que retorne o valor máximo das colunas da
matriz
d. Calcule a soma dos elementos em cada coluna da matriz
e. Calcule a soma dos elementos em cada linha da matriz
f. Calcule o produto entre os elementos de cada coluna da matriz.
"""
import numpy as np

mat = np.random.randint(-5, 6, size=(4, 3))
abs_mat = np.abs(mat)
print(abs_mat)

seno_primeira_linha = np.sin(mat[0])
print(seno_primeira_linha)

max_colunas = np.max(mat, axis=0)
print(max_colunas)

soma_colunas = np.sum(mat, axis=0)
print(soma_colunas)

soma_linhas = np.sum(mat, axis=1)
print(soma_linhas)

produto_colunas = np.prod(mat, axis=0)
print(produto_colunas)
