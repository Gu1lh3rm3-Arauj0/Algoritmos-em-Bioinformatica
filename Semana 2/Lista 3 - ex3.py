"""
Exercicio 3 - Semana 2-2
3)Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""
A = input('Informe a string: ')

for i in range(len(A)):
    B = A.count(A[i])
    print(f'{A[i]}: {B}X')