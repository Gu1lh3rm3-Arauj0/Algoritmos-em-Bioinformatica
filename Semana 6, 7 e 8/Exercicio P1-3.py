"""
Guilherme Araujo Mendes de Souza - 156437
Prova de Algoritmos em bioinformática
Exercicio 3
"""
def funcao(a):
    e = 2.71828182
    n = 1

    while (((1/e) - (((1)-(1/n))**n)) > a):
        n += 1
    
    b = ((1/e) - (((1)-(1/n))**n))
    
    return[b, n]

x = float(input('Informe o valor de aproximação: '))
print(funcao(x))