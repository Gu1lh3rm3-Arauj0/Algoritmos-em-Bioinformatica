# -*- coding: utf-8 -*-
"""
Semana 4-1
Guilherme Araújo Mendes de Souza - 156437
UNIFESP - ICT
alg bio

Crie um programa que gerencia o aproveitamento de um
jogador de futebol. o programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário incluindo o total de
gols realizados durante o campeonato
"""

dic = {}

nome = input('Infome o nome do Jogador: ')
partidas = int(input(f'Informe o número de partidas jogadas pelo {nome}: '))
gols = int(input(f'informe o número de gols realizados pelo {nome}: '))

dic = {"Nome": nome, "Número de partidas": partidas, "Número de gols": gols}

print(dic)