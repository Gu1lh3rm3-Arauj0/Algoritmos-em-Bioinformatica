"""
Guilherme Ara√∫jo Mendes de Souza 
UNIFESP - ICT
AlgBio

Lista 8 - Exercicio 1
Crie um array unidimensional com valores aleat√≥rios e imprima o
valor m√©dio e a mediana.
"""
#import random
import numpy as np

v = np.random.randint(1,100,(1,10))

print(v)
print(f'A media È {np.mean(v)}')
print(f'A mediana È {np.median(v)}')
