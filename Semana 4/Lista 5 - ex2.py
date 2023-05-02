"""
Semana 4-1
Guilherme Araújo Mendes de Souza - 156437
UNIFESP - ICT
alg bio

Crie um programa que leia nome, sexo, peso e altura de
várias pessoas. guarde os dados de cada pessoa num
dicionário individual e acrescente o IMC da pessoa.
Organize todos os dicionários em uma lista. No final
mostre
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas
"""

lista = []
media_peso = 0
media_altura = 0
media_imc = 0

k = (int(input('Informe o número de pessoas: ')))

for i in range(k):
    nome = input('Informe o nome da pessoa: ')
    sexo = input('Informe o sexo da pessoa: ')
    peso = float(input('Informe o peso da pessoa: '))
    altura = float(input('Informe a altura da pessoa: '))
    imc = (peso)/(altura**2)
    dic = {"nome": nome, "sexo": sexo, "peso": peso, "altura": altura, "imc": imc}
    lista.append(dic)

for i in lista:
    peso = i['peso']
    altura = i['altura']
    imc = i['imc']
    media_peso += peso
    media_altura += altura
    media_imc += imc

media_peso /= len(lista)
media_altura /= len(lista)
media_imc /= len(lista)

print(f'Total de pessoas cadastradas: {k}')
print(f'Peso médio das pessoas: {media_peso: .2f}')
print(f'Altura média das pessoas: {media_altura: .2f}')
print(f'IMC médio das pessoas: {media_imc: .2f}')