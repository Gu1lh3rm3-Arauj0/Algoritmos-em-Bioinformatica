"""
Guilherme Araujo Mendes de Souza - 156437
Desafio - criptografia
"""

a = input(str('Informe uma frase: '))

for i in range(25):
    lista = []
    for j in a:
        if((ord(j) > 64) and (ord(j) < 91)) or ((ord(j) > 96) and (ord(j) < 123)):
            num=ord(j)
            num=num+i
            if(num>122):
                num=num-26
            lista.append(chr(num))
            c = [str(i) for i in lista]
        else:
            num=ord(j)
            lista.append(chr(num))
            c = [str(i) for i in lista]
    print(''.join(c))
    print(i)
    print('')