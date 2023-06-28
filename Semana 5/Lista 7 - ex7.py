"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
algbio

Lista 7 - Exercico 7
Crie uma função que faça a leitura deste arquivo json e tenha como saída um
dicionário da mesma forma que do item 1.
"""

import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dicionario = json.load(arquivo)
        return dicionario
    except Exception as e:
        print(f"Erro ao ler o arquivo JSON: {str(e)}")
        return {}

# Chamar a função ler_json para ler o arquivo JSON e obter o dicionário
dicionario_lido = ler_json('dados.json')  # Substitua 'dados.json' pelo nome do arquivo que deseja ler

# Imprimir o dicionário lido
print(dicionario_lido)

