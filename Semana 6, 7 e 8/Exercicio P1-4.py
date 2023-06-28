#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guilherme Araujo Mendes de Souza - 156437
Prova de Algoritmos em bioinformática
Exercicio 4
"""

def fatorial(x):
    if x>1:
        return x*fatorial(x-1)
    else:
        return 1

def seno(x):
    sen = 0
    for i in range (0, 30):
        sen = sen + ((1/fatorial(2*i+1))*(x**(2*i+1)))

    return sen

a = int(input('Informe um valor'))

print(seno(a))