'''
Guilherme Araújo Mendes de Souza - 156437
Desafio – criptografia
'''

import random as r

a = input(str('Informe uma frase: '))
k = r.randint(1,25)
lista = []

for i in a:
    num=ord(i)
    num=num+k
    if(num>122):
        num=num-26
    lista.append(chr(num))

print('Mensagem criptografada com k= ', k)

c = [str(i) for i in lista]
print(''.join(c))