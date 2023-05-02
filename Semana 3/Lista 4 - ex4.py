"""
Exercicio 4 - Semana 3
Faça um Programa que leia 20 números inteiros e
armazene-os num lista. Armazene os números pares na lista
PAR e os números IMPARES na lista impar. Imprima os três
vetores.
"""
lista=[]
lista_par=[]
lista_impar=[]
for i in range (1, 21):
    lista.append(i)

for i in range(1, len(lista)):
    if lista[i]%2==0:
        lista_par.append(lista[i])
    elif lista[i]%2!=0:
        lista_impar.append(lista[i])

print(lista)
print(lista_par)
print(lista_impar)