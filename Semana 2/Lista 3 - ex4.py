"""
Exercicio 4 - Semana 2-2 
4)Escreva um programa que leia três strings. Imprima o resultado da
substituição na primeira, dos caracteres da segunda pelos da terceira.
1a string: AATTCGAA
2a string: TG
3a string: AC
Resultado: AAAACCAA
"""
A = input('Informe a string: ')
B = input('Informe a string: ')
C = input('Informe a string: ')
result = A.replace(B[0], C[0])
result = result.replace(B[1],C[1])
print(result)
