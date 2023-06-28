"""
Guilherme Araujo Mendes de Souza - 156437
Prova de Algoritmos em bioinformática
Exercicio 2
"""

def funcao(x):
    a = ''
    if x != x[::-1]:
        a = x
    return a
    

lista = []
lista_nova = []


k = int(input('Informe quantas palavras você quer adcionar a Lista: '))

for i in range (k):
    lista.append(input('Informe a palavra: '))

for i in lista:
    lista_nova.append(funcao(i))

print(f'Nova lista {lista_nova}')
