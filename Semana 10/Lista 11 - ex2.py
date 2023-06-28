"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Algoritmo de Divisão e Conquista (Ordenação por Fusão)
Implemente um programa que utilize o algoritmo de ordenação por fusão
(merge sort) para ordenar uma lista de valores inteiros.
"""

def merge_sort(lista):
    # Verifica se a lista está vazia ou contém apenas um elemento
    if len(lista) <= 1:
        return lista
    
    # Divide a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Recursivamente ordena as sublistas
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Mescla as sublistas ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Mescla as sublistas comparando os elementos em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes da sublista esquerda, se houver
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    # Adiciona os elementos restantes da sublista direita, se houver
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado

lista = [7, 2, 9, 1, 6]

lista_ordenada = merge_sort(lista)
print(f"Lista ordenada: {lista_ordenada}")
