"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 10 - Exercicio 4
Crie uma função na qual calcula o valor do cos a partir da série de Taylor
(50 primeiros termos) e seno a partir da seguinte identidade. Obs: Fazer
a serie sem utilizar for/ while. Utilizar a função factorial da biblioteca scipy
"""

import numpy as np
from scipy.special import factorial

def cos_taylor(x):
    # Converter o ângulo para radianos
    x_rad = np.radians(x)
    
    # Calcular o valor do cosseno usando a série de Taylor
    cos_value = np.sum((-1)**np.arange(50) * x_rad**(2*np.arange(50)) / factorial(2*np.arange(50)))
    
    return cos_value


def sen_taylor(x):
    # Converter o ângulo para radianos
    x_rad = np.radians(x)
    
    # Calcular o valor do seno usando a série de Taylor
    sen_value = np.sum((-1)**np.arange(50) * x_rad**(2*np.arange(50) + 1) / factorial(2*np.arange(50) + 1))
    
    return sen_value



cos_value = cos_taylor(45)
print("Cosseno:", cos_value)

sen_value = sen_taylor(45)
print("Seno:", sen_value)

