"""
Guilherme Araújo Mendes de Souza - 156437
Exercicio 1 - Semana 4-

Faça um programa que leia o nome RA e média final de
uma aluno. Armazene todas as informações num
dicionário. No final programa deve imprimir as
informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.
"""

a = {}
nome = []
RA = []
MediaFinal = []
result = []

k = int(input('Informe o Numero de Alunos: '))

for i in range (k):
    nome.append(input('Informe o nome do aluno: '))
    RA.append(input('Informe o numero do RA do Aluno: '))
    MediaFinal.append(int(input('Informe a media final do Aluno: ')))
    if MediaFinal[i] >= 6:
        result.append('Aprovado')
    else:
        result.append('Reprovado')
    
    
    a = {"nome": nome, "RA": RA, "Media Final": MediaFinal, "result": result}
    
for i in range(k):
    print("Nome: ", a["nome"][i], end=", ")
    print("RA:", a["RA"][i], end=", ")
    print("Media Final:", a["Media Final"][i], end=", ")
    print("Resultado:", a["result"][i])