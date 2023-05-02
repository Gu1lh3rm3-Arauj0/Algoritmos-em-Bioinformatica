"""
Semana 4-1
Guilherme Araújo Mendes de Souza - 156437
UNIFESP - ICT
alg bio

Crie um programa que leia o nome, ano de nascimento e
carteira de trabalho e cadastre-os com idade em um
dicionario. se por acaso a CTPS for diferente de zero o
dicionario recebera tambem o ano de contratação e
salario. Calculo e acrescente além da didade, com
quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

dic = {}

nome = input('Informe o Nome: ')
ano_nascimento = int(input('Informe o ano de nascimento: '))
mes_nascimento = int(input('Informe o mês de nascimento: '))
dia_nascimento = int(input('Informe o dia de nascimento: '))
data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento, 0, 0, 0)
data_atual = datetime.today()
idade = int((datetime.now() - data_nascimento).days / 365.25)
ctps = int(input('Informe a CTPS: '))
if ctps != 0:
    ano_contracao = int(input('Informe o ano de contração: '))
    salario = float(input('Informe o salário: '))
    ano_atual = datetime.now().year
    aposentar = ano_contracao - ano_atual + 35 + idade
    dic = {"nome": nome, "ano de nascimento": data_nascimento, "idade": idade, "ctps": ctps, "ano de contração": ano_contracao, "salario": salario, "aposentar": aposentar}
else:
    dic = {"nome": nome, "ano de nascimento": data_nascimento, "idade": idade, "ctps": ctps}

print(dic)