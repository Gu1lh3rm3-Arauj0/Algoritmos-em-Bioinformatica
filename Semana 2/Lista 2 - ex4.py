"""
Exercicio 4 - Semana 2
"""
B = str()
print('Belamatematica')
for i in range (1, 10):
    A = B + str(i)
    result = int(A)*8+i
    print(f'{A} x 8 + {i} = {result}')
    B = A    