"""
Exercicio 1 - Semana 2-2
1)Escreva um programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início.
1a string: AABBEFAATT
2a string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""
A = 'AABBEFAATT'
B = 'BE'

print(f'{B} encontrado na posição {A.find(B)} de {A}')