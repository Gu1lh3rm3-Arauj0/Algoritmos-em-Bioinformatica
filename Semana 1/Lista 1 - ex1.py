nome = input('Digite o seu nome: ')
idade = float(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))

print('A idade do', nome, 'é', idade, 'e a sua altura é', altura)
print('A idade do {} é {} e a sua altura é {}'.format(nome,idade,altura))
print(f'A idade do {nome} é {idade} e a sua altura é{altura}')
