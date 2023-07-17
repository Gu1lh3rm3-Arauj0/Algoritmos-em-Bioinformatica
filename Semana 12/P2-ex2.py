"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Prova
Exercicio 2
"""

import numpy as np
from scipy.special import factorial

def sen_taylor(x):
    # Calcular o valor do seno usando a série de Taylor
    sen = np.sum(1/(factorial(2*np.arange(30) + 1))*(x**(2*np.arange(30) + 1)))
    #Eu Estava passando o angulo para RAD
    return sen

def e(x):
    e_value = np.sum(x**np.arange(30)/factorial(np.arange(30)))
    #Esqueci de elevar por np.arange(30)
    #Esqueci de Usar factorial(np.arange(30))
    
    return e_value

x = float(input())

sen_value = sen_taylor(x)
e_value = e(x)
print("Seno:", sen_value)
print("E^x:", e_value)
print(f"Cosseno: {e_value-sen_value}")

