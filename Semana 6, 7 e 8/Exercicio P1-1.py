"""
Guilherme Araujo Mendes de Souza - 156437
Prova de Algoritmos em bioinformática
Exercicio 1
"""
lista = []
media_imc = 0
a = 0
b = 0
c = 0

k = int(input('Informe o número de pessoas: '))

for i in range(k):
    nome = input('Informe o nome: ')
    sexo = input('Informe o sexo da pessoa: ')
    peso = float(input('informe o peso da pessoa: '))
    altura = float(input('informe a altura da pessoa: '))
    imc = (peso)/(altura**2)
    if imc <=24.9:
         a = a + 1
         situacao = 'Peso normal'
    elif imc >= 25 and imc <= 29.9:
        b = b + 1
        situacao= 'Sobrepeso'
    else:
        situacao = 'obesidade'
        c = c + 1
    dic = {"nome": nome, "sexo": sexo, "peso": peso, "altura": altura, "imc": imc, "situacao": situacao}
    lista.append(dic)

for i in lista:
    peso = i['peso']
    altura = i['altura']
    imc = i['imc']
    media_imc += imc


media_imc /= len(lista)

print(f'Total de pessoas cadastradas: {k}')
print(f'IMC médio das pessoas: {media_imc: .2f}')
print(f'Em situação de peso normal: {a} ')
print(f'Em situação de sobrepeso: {b}')
print(f'Em situação de Obesidade: {c}')
    
        