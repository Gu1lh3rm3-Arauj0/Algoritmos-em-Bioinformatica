"""
Guilherme Araújo Mendes de Souza 
UNIFESP - ICT
AlgBio

Lista 8 - Exercicio 1
Crie um array unidimensional com valores aleatórios e imprima o
valor médio e a mediana.
"""
#import random
import numpy as np

v = np.random.randint(1,100,(1,10))

print(v)
print(f'A media � {np.mean(v)}')
print(f'A mediana � {np.median(v)}')
