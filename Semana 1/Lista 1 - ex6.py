# -*- coding: utf-8 -*-
"""
A resistência combinada de três resistores R1, R2 e R3 em
paralelo é dada por (Imagem) Crie três variáveis com três valores de resistências e calcule a
resistência resultante.
"""
R1 = float(input('Informe o valor do primeiro resistor: '))
R2 = float(input('Informe o valor do segundo resistor: '))
R3 = float(input('Informe o valor do terceiro resistor: '))

Rresult = 1/((1/R1)+(1/R2)+(1/R3))

print(f'A resistencia resultante é: {Rresult}')