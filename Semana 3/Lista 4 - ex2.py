"""
Exercico 2 - Semana 3
Faça um programa que leia duas listas e que gere uma
terceira com os elementos das duas primeiras.
"""
Lista1 = []
Lista2 = []
Lista3 = []

A = int(input('Informe o número de elementos da lista A'))
B = int(input('Informe o número de elementos da lista B'))

for i in range (1, A+1):
    Lista1.append(i)
for i in range (1, B+1):
    Lista2.append(i)
Lista3.append(Lista1 + Lista2)
print(Lista3)

## Lista3 = Lista1.extend(Lista2)