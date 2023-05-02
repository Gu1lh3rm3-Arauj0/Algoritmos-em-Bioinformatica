"""
Escreva um script que leia a quantidade de dias,horas,
minutos e segundos para o usuário. Calcule o total em
segundos.
"""
dias = int(input('Informe os dias: '))
horas = int(input('Informe os horas: '))
minutos = int(input('Informe os minutos: '))
segundos = int(input('Informe os segundos: '))

total = (dias*24*60*60) + (horas*60*60) + (minutos*60) + (segundos)

print(f'O total de segundos é: {total}')