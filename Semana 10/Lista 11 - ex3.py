"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 11 - Exercicio 3
Algoritmo Guloso (Problema da Mochila Fracionária)
Implemente um programa que, dado um conjunto de objetos com pesos e
valores, encontre a melhor combinação de objetos para colocar em uma mochila
com uma capacidade máxima, maximizando o valor total. Neste caso, os objetos
podem ser fracionados.
"""

def mochila_fracionaria(capacidade, objetos):
    # Calcula a relação valor/peso para cada objeto
    valores_por_peso = [(valor / peso, peso, valor) for peso, valor in objetos]
    
    # Ordena os objetos em ordem decrescente da relação valor/peso
    valores_por_peso.sort(reverse=True)
    
    # Inicializa a capacidade restante da mochila e o valor máximo alcançado
    capacidade_restante = capacidade
    valor_maximo = 0
    
    # Percorre os objetos em ordem decrescente da relação valor/peso
    for relacao, peso, valor in valores_por_peso:
        # Verifica se ainda há capacidade na mochila
        if capacidade_restante > 0:
            # Calcula a quantidade fracionária do objeto que pode ser colocada na mochila
            quantidade = min(1, capacidade_restante / peso)
            
            # Atualiza a capacidade restante da mochila
            capacidade_restante -= quantidade * peso
            
            # Atualiza o valor máximo alcançado
            valor_maximo += quantidade * valor
    
    return valor_maximo

capacidade = 50
objetos = [(60, 10), (100, 20), (120, 30)]

valor_maximo = mochila_fracionaria(capacidade, objetos)
print(f"Valor máximo alcançado: {valor_maximo}")
