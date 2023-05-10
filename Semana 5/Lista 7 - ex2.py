"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 7 - Exercicio 2
Crie uma função, chamada complementar, na qual tenha como entrada o dicionário da item 1 e calcule a fita complementar da chave seq. A saída desta função será uma string
"""
from lista import dados

def complementar():
    arquivo = open('seq_a.fasta', 'r')
    conteudo = arquivo.read()
    arquivo.close()

    # Separar o cabeçalho da sequência
    linhas = conteudo.split('\n')
    cabecalho = linhas[0]
    sequencia = ''.join(linhas[1:])

    # Gerar a sequência complementar
    complemento = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complementar = ''.join([complemento[base] for base in sequencia])

    return complementar

sequencia_complementar = complementar(dados)
print(sequencia_complementar)