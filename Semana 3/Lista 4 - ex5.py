"""
Exercicio 5 - Semana 3
Faça um Programa que peça as quatro notas de 5 alunos,
calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a
7.0
"""
media=[]
count = 0
for i in range(0, 5):
    A = 0
    for j in range (0, 4):
        B = float(input(f'Informe as notas da {j+1} Prova: '))
        A = A + B
    media.append(A/4)
#print(media.count([i]>=7.0))
for i in media:
    if media[i]>=7:
        count = count + 1
print(count)
        