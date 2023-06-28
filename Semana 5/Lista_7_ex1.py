"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 7 - Exercicio 1
Crie uma função na qual faça a leitura de um arquivo fasta chamado Corona_genomic.fasta e armazene em um dicionário com as chaves seq_DNA e descrição
"""

def leitura():
    arquivo = open('Corona_genomic.fasta', 'r')
    dados = {}
    seq_atual = ''
    
    for linha in arquivo:
        if linha.startswith('>'):
            descricao = linha.strip().replace('>', '')
            dados[descricao] = ''
            seq_atual = descricao
        else:
            dados[seq_atual] += linha.strip()
            
    arquivo.close()
    
    return dados

dados = {}

dados = leitura()

print(dados)