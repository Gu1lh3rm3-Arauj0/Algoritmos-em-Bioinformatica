# -*- coding: utf-8 -*-
"""
Escreva um script que pergunte a quantidade de km
percorridos por um carro alugado pelo usuário e a
quantidade de dias pelo qual o carro foi alugado. Calcule o
preço a pagar sabendo que o carro custa 60 reais por dia e
15 centavos por Km rodado.
"""

km = float(input('Quantos KM foram rodados com o carro: '))
dias = int(input('Por quantos dias o carro foi alugado: '))

valor = (km*0.15)+(dias*60)

print(f'O valor total a ser pago é {valor: .2f}')