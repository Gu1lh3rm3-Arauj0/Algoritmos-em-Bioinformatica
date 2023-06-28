"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
algbio

Lista 7 - Exercicio 5
Crie uma função, chamada compare, na qual tem como entrada 2 dicionarios
do item 1 e realize a comparação das sequencias de DNA. Esta função deve
imprimir a quantidade de nucleotídeos alterados e quais posições foram
realizados as trocas. 
"""

from Lista_7_ex1 import dados

def compare(dicionario1, dicionario2):
    sequencia1 = dicionario1.get('seq_DNA', '')  # Obter a sequência de DNA do primeiro dicionário, se presente
    sequencia2 = dicionario2.get('seq_DNA', '')  # Obter a sequência de DNA do segundo dicionário, se presente

    # Verificar se as sequências foram fornecidas
    if not sequencia1 or not sequencia2:
        print("Erro: sequências de DNA não fornecidas em ambos os dicionários.")
        return

    # Verificar se as sequências têm o mesmo comprimento
    if len(sequencia1) != len(sequencia2):
        print("Erro: as sequências de DNA têm comprimentos diferentes.")
        return

    # Inicializar contador de nucleotídeos alterados
    nucleotideos_alterados = 0

    # Listar as posições em que ocorreram trocas
    posicoes_trocas = []

    # Comparar as sequências de DNA
    for i in range(len(sequencia1)):
        if sequencia1[i] != sequencia2[i]:
            nucleotideos_alterados += 1
            posicoes_trocas.append(i)

    # Imprimir o resultado
    print(f"Quantidade de nucleotídeos alterados: {nucleotideos_alterados}")
    if nucleotideos_alterados > 0:
        print("Posições das trocas:")
        for posicao in posicoes_trocas:
            print(posicao)

# Chamar a função compare com dois dicionários como entrada
compare(dados, dados)  # Substitua o segundo argumento pelo segundo dicionário que você deseja comparar
