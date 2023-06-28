"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
algbio

Lista 7 - Exercicio 4
Crie uma função, chamada freq, na qual tem como entrada o dicionário
criando no item 1 e faça o cálculo das frequências, porcentuais de
aminoácidos da chave seq_DNA. Esta função deve imprimir os resultados das
frequências assim como adicionar, chaves Fa,Fc,Ft,Fg, ao dicionário de
entrada.
"""
from Lista_7_ex1 import dados

def freq(dicionario):
    arquivo = dicionario.get('seq_a.Fasta', '')  # Obter o nome do arquivo do dicionário, se presente

    # Verificar se o nome do arquivo foi fornecido
    if arquivo:
        try:
            with open(arquivo, 'r') as f:
                sequencia = f.read().strip()  # Ler a sequência do arquivo e remover espaços em branco
        except FileNotFoundError:
            print(f"Erro: arquivo '{arquivo}' não encontrado.")
            return dicionario
    else:
        print("Erro: nome do arquivo não fornecido.")
        return dicionario

    # Inicializar contadores para cada aminoácido
    contador_a = 0
    contador_c = 0
    contador_t = 0
    contador_g = 0

    # Calcular as frequências de cada aminoácido na sequência
    for aminoacido in sequencia:
        if aminoacido == 'A':
            contador_a += 1
        elif aminoacido == 'C':
            contador_c += 1
        elif aminoacido == 'T':
            contador_t += 1
        elif aminoacido == 'G':
            contador_g += 1

    total_aminoacidos = contador_a + contador_c + contador_t + contador_g

    # Calcular as frequências percentuais
    frequencia_a = (contador_a / total_aminoacidos) * 100
    frequencia_c = (contador_c / total_aminoacidos) * 100
    frequencia_t = (contador_t / total_aminoacidos) * 100
    frequencia_g = (contador_g / total_aminoacidos) * 100

    # Adicionar as chaves de frequência ao dicionário de entrada
    dicionario['Fa'] = frequencia_a
    dicionario['Fc'] = frequencia_c
    dicionario['Ft'] = frequencia_t
    dicionario['Fg'] = frequencia_g

    # Imprimir os resultados das frequências
    print(f'Frequência de A: {frequencia_a}%')
    print(f'Frequência de C: {frequencia_c}%')
    print(f'Frequência de T: {frequencia_t}%')
    print(f'Frequência de G: {frequencia_g}%')

    return dicionario

dados_atualizados = freq(dados)

print(dados_atualizados)