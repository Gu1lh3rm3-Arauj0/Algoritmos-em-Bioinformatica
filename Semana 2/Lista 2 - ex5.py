"""
Exercicio 5 - Semana 2
"""
a = float(input('Informe o valor de a: '))
e = 2.71828182

n = 1

while (((1/e) - (((1)-(1/n))**n)) > a):
    n += 1
#result = (((1)-(1/n))**n)
print(f'Foram necessárias {n} tentativas para o valor se aproximar da constante {1/e: .8f}')