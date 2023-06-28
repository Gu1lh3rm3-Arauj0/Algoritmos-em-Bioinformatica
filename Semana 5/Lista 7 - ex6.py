"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
algbio

Lista 7 - Exercicio 6
Crie uma função que salve o dicionário criado no item 1 em um arquivo do
tive json. Dica procure no google ou chatgpt o que é um arquivo do tipo json.
"""
import json
from Lista_7_ex1 import dados

def salvar_json(dicionario, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dicionario, arquivo, indent=4)
        print(f"Dicionário salvo com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar o dicionário: {str(e)}")

# Chamar a função salvar_json para salvar o dicionário em um arquivo JSON
salvar_json(dados, 'dados.json')  # Substitua 'dados.json' pelo nome do arquivo que você deseja salvar

