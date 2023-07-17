"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Prova
Exercicio 1
"""

def leitura():
    arquivo = open('multifasta.fasta', 'r')
    dados = {}
    seq_atual = ''
    
    
    for linha in arquivo:
        if linha.startswith('>'):
            descricao = linha.strip().replace('>', '')
            dados[descricao] = ''
            seq_atual = descricao
        else:
            dados[seq_atual] += linha.strip()
            contador_a = 0
            contador_c = 0
            contador_t = 0
            contador_g = 0
            
            for aminoacido in dados[seq_atual]:
                if aminoacido == 'A':
                    contador_a += 1
                elif aminoacido == 'C':
                    contador_c += 1
                elif aminoacido == 'T':
                    contador_t += 1
                elif aminoacido == 'G':
                    contador_g += 1
            
            total_aminoacidos = contador_a + contador_c + contador_t + contador_g
            
            frequencia_a = (contador_a / total_aminoacidos) * 100
            frequencia_c = (contador_c / total_aminoacidos) * 100
            frequencia_t = (contador_t / total_aminoacidos) * 100
            frequencia_g = (contador_g / total_aminoacidos) * 100
            
            dados['Fa'] = frequencia_a
            dados['Fc'] = frequencia_c
            dados['Ft'] = frequencia_t
            dados['Fg'] = frequencia_g
            
            print(f'O tamanho é: {total_aminoacidos}')
            print(f'Frequência de A: {frequencia_a}%')
            print(f'Frequência de C: {frequencia_c}%')
            print(f'Frequência de T: {frequencia_t}%')
            print(f'Frequência de G: {frequencia_g}%')
        
    arquivo.close()
    
    
    return dados

dados = {}

dados = leitura()
    
print(dados)

# Faltou só colocar os dados dentro do for