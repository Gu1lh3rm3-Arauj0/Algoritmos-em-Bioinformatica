"""
Faça um script que calcule o aumento de salário. Ele deve
solicitar o valor do salário e a porcentagem de aumento.
Exiba o valor do aumento e do novo salário.
"""
atual = float(input('Informe o valor do seu salário atual: '))
aumento = float(input('Informe a porcentagem de aumento do salário'))

novo = ((atual*aumento)/100)+atual

print(f'O seu salário atual é: {novo: .2f}')