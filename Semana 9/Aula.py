"""
Guilherme Araújo Mendes de Souza - 156437
UNIFESP - ICT
AlgBio

Aula do dia 15/05/2023
"""
import numpy as np
from scipy.special import factorial

def f2(x):
    if x>1:
        return x*f2(x-1)
    else:
        return 1

a = int(input('Informe o valor: '))
print(f2(a))

m = [[1,2], [3,4]]

mm = np.array(m)

mm.ndim

mm.dtype

mm.size

a = np.ones((4, 4, 4))

b = 2*np.ones((4, 4, 4))

c = np.linspace(0, 10, 10)

d = np.random.rand(3,4)

e = np.random.randint(1, 15,(3,3))

e.dtype('int32')

e.astype('float32')

e.astype('complex64')

###################################################################################

n = np.arange(0,31)
x = 1
a = (x*np.ones(30))**n
b = f2(n)
b = 1/b

e = a@b

####################################################################################
n = np.arange

