# -*- coding: utf-8 -*-
"""
Desafio - Semana 2
Faça um código em python que solicite ao usuário um
numero inteiro e diga se ele é um numero primo.
"""
cont = 0
A = int(input('Informe um número: '))

for i in range (1, A+1):
    if A%i == 0:
        cont += 1
if cont == 2:
    print(f'O número {A} é primo')
elif cont > 2:
    print(f'O número {A} não é primo')