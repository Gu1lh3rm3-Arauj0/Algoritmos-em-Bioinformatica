"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 11 - Exercicio 1
Algoritmo Guloso (Problema da Troca de Moedas)
Implemente um programa que, dado um valor inteiro N e um conjunto de
moedas de valores diferentes, encontre a menor quantidade de moedas
necessárias para representar o valor N. Considere que há um número infinito de
moedas de cada valor disponível.
"""

def troca_de_moedas(N, moedas):
    # Ordena as moedas em ordem decrescente
    moedas = sorted(moedas, reverse=True)
    
    # Inicializa a quantidade mínima de moedas utilizadas como 0
    quantidade_minima = 0
    
    # Percorre as moedas disponíveis
    for moeda in moedas:
        # Enquanto o valor da moeda for menor ou igual ao valor restante a ser formado
        while moeda <= N:
            # Subtrai o valor da moeda do valor restante
            N -= moeda
            # Incrementa a quantidade mínima de moedas utilizadas
            quantidade_minima += 1
    
    return quantidade_minima

N = 36
moedas = [1, 5, 10, 25]

quantidade_minima = troca_de_moedas(N, moedas)
print(f"Quantidade mínima de moedas: {quantidade_minima}")
