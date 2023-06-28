"""
Guilherme Araújo Mendes de Souza
UNIFESP - ICT
algbio

Lista 7 - Exercicio 3
Crie uma função, chamada transcrição, na qual tenha como entrada o
dicionário do item 1 e calcule o mRNA da chave seq. A saída desta função
será o próprio dicionário de entrada adicionado a chave seq_RNA
"""

from Lista_7_ex1 import dados

def transcricao(dicionario):
    sequencia = dicionario.get('seq', '')  # Obter a sequ�ncia do dicion�rio, se presente

    # Realizar a transcri��o do DNA para RNA
    transcrito = sequencia.replace('T', 'U')

    # Adicionar o mRNA ao dicion�rio
    dicionario['seq_RNA'] = transcrito

    return dicionario

# Chamar a fun��o transcricao com o dicion�rio como entrada
dados_atualizados = transcricao(dados)

# Imprimir o dicion�rio atualizado
print(dados_atualizados['seq_RNA'])
        