"""
Exercicio 2 - Semana 2-2
2)Escreva um programa que leia duas strings e gere uma terceira com os
caracteres comuns às duas strings lidas.
1a string: AAACTBF
2a string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve
conter todas as letras comuns a ambas.
"""

A = input('Informe a primeira string: ')
B = input('Informe a segunda string: ')
C = ''

for i in range(len(B)):
    for j in range(len(A)):
        if A[j] == B[i]:
            C = C + A[j]
print(C)