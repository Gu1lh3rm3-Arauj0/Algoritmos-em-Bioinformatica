"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 11 - Exercicio 4
Algoritmo de Divisão e Conquista (Pesquisa Binária)
Implemente um programa que utilize o algoritmo de pesquisa binária para
encontrar um elemento em uma lista ordenada de valores inteiros. O programa
deve retornar a posição do elemento na lista ou -1 caso não seja encontrado.
"""

def pesquisa_binaria(lista, elemento):
    # Define os índices inicial e final da lista
    inicio = 0
    fim = len(lista) - 1
    
    # Realiza a pesquisa enquanto o intervalo for válido
    while inicio <= fim:
        # Calcula o índice do elemento do meio do intervalo
        meio = (inicio + fim) // 2
        
        # Verifica se o elemento do meio é igual ao elemento procurado
        if lista[meio] == elemento:
            return meio  # Retorna a posição do elemento
        
        # Se o elemento do meio for maior que o elemento procurado,
        # atualiza o índice final para o elemento anterior ao meio
        elif lista[meio] > elemento:
            fim = meio - 1
        
        # Se o elemento do meio for menor que o elemento procurado,
        # atualiza o índice inicial para o elemento posterior ao meio
        else:
            inicio = meio + 1
    
    return -1  # Retorna -1 se o elemento não for encontrado

lista = [1, 4, 6, 9, 13, 20, 22]
elemento = 9

posicao = pesquisa_binaria(lista, elemento)
print(f"Posição do elemento: {posicao}")
