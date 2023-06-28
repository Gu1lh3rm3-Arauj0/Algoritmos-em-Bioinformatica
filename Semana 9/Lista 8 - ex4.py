# -*- coding: utf-8 -*-
"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 8 - Exercicio 4
Crie um array unidimensional com valores aleatórios e calcule a
diferença entre cada elemento e o próximo elemento.
"""
import numpy as np

array = np.random.randint(1, 10, 5)  # Substitua 5 pelo tamanho desejado do array e ajuste os limites dos valores aleatórios conforme necessário
print("Array original:", array)

# Calcular a diferença entre cada elemento e o próximo elemento
diferencas = np.diff(array)
print("Diferenças:", diferencas)