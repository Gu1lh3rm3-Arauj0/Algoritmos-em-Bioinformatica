""", ,, 
Desafio , semana 3-3
gerar um CPF 
"""
import random

cpf = []

for i in range(9):
    cpf.append(random.randint(0,9))
##print(cpf)

soma = 0

for i,j in zip(range(0, 9 +1), range (10, 1, -1)): 
    soma = soma + (cpf[i]*j)
##print(soma)
d1 = (11 - soma)%11
cpf.append(d1)

soma = 0

for i,j in zip(range(1, 10, +1), range (10, 1, -1)): 
    soma = soma + (cpf[i]*j)
d2 = (11 - soma)%11
cpf.append(d2)

a = [str(i) for i in cpf]

print(''.join(a))