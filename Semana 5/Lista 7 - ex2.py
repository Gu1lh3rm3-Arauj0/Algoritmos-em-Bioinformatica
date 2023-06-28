"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 7 - Exercicio 2
Crie uma função, chamada complementar, na qual tenha como entrada o dicionário da item 1 e calcule a fita complementar da chave seq. A saída desta função será uma string
"""
from Lista_7_ex1 import dados

def complementar(dicionario):
    sequencia = dicionario.get('seq', '')  # Obter a sequência do dicionário, se presente

    # Gerar a sequência complementar
    complemento = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequencia_complementar = ''.join([complemento.get(base, '') for base in sequencia])

    return sequencia_complementar

# Chamar a função complementar com o dicionário como entrada
sequencia_complementar = complementar(dados)

# Imprimir a sequência complementar
print(sequencia_complementar)