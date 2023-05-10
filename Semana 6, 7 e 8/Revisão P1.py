"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Revisão - P1
Esse codigo tem intuito de servir de revisão para a prova de Algoritmos em BioInformática
portanto o mesmo não tem funcionalidade
"""
#Input
str = input('Input para string')
int = int(input('Input para inteiros'))
float = float(input('Input para reais'))

#Print
nome = 'Guilherme'
idade = 21
altura = 1.90
print('A idade do', nome, 'é', idade, 'e a sua altura é', altura)
print('A idade do {} é {} e a sua altura é {}'.format(nome,idade,altura))
print(f'A idade do {nome} é {idade} e a sua altura é{altura}')

#Variaveis Primitivas
    #str, int, float e booleana(True ou False)
        #booleana em If
a = True

if a:
    print("a é verdadeiro")
else:
    print("a é falso")
#Vai imprimir que a é verdadeiro

#string 
    #join() - Esse comando serve para unir as strings de uma lista
palavras = ['olá', 'mundo', 'como', 'vai']
frase = ' '.join(palavras)
print(frase)  # saída: 'olá mundo como vai'

frase = ', '.join(palavras)
print(frase)  # saída: 'olá, mundo, como, vai'

    #split() - Esse comando serve para dividir uma string em uma Lista
frutas = "banana,maçã,uva"
lista_frutas = frutas.split(",")
print(lista_frutas) #["banana", "maçã", "uva"]

texto = "Isso é um exemplo"
lista_palavras = texto.split(3)
print(lista_palavras) #["Iss", "o é", " um", " ex", "emp", "lo"]

    #fateamento de string - string[inicio:fim], onde inicio é onde eu começo o fateamento e fim é onde eu termino e fateamento
string = "abcdefghij"
print(string[2:5])   # resultado: "cde"
print(string[:5])    # resultado: "abcde"
print(string[7:])    # resultado: "hij"
print(string[1:8:2])   # resultado: "bdfh"

#operadores aritmeticos
    # Adição (+)
    # Subtração (-)
    # Multiplicação (*)
    # Divisão (/)
    # Divisão inteira (//)
    # Resto da divisão ou módulo (%)
    # Potenciação (**)

#comando if
    #operadores:
        # Igual (==)
        # Diferente (!=)
        # Menor (<)
        # Maior (>)
        # Menor igual (<=)
        # Maior Igual (>=)
        # e (and)
        # ou (or)
r = 2
if r == 1:
    print('r não é igual a 1')
elif r== 2:
    print('r é igual a 2')  
else:
    print('r não é igual a 1 ou 2')     
    
#comandos de Loop
#for
for i in range(1, 6, 1): #(inicio, fim, passo) ele não vai até o 6
    print(i)
    
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)
    
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
for i in dicionario:
    print(i) 
    #Vai imprimir: 
        #chave1
        #chave2
        #chave3

for i in dicionario.keys():
    print(i) 
    #Vai imprimir: 
        #chave1
        #chave2
        #chave3

for i in dicionario.values():
    print(i)
    #Vai imprimir: 
        #valor1
        #valor2
        #valor3

for i, j in dicionario.items():
    print(i, j)
    #Vai imprimir: 
        #chave1 valor1
        #chave2 valor2
        #chave3 valor3

    #comando zip
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

for x, y, z in zip(a, b, c):
    print(x, y, z)
    #vai imprimir:
        #1 a True
        #2 b False
        #3 c True

    #comando enumerate
lista2 = ['a', 'b', 'c', 'd']
for i, elemento in enumerate(lista2):
    print(i, elemento)
    #vai imprimir:
        #0 a
        #1 b
        #2 c
        #3 d

#while
g = 1
while g <= 5:
    print(g)
    g += 1

while g >= 5:
    print(g)
    g -= 1

while g != 5:
    print(g)
    g += 1

g = 1
while g == 1:
    print(g)
    g += 1

#Lista
'''
Em Python, uma lista é um tipo de estrutura de dados que permite armazenar uma coleção ordenada de valores, sejam eles de tipos diferentes. As listas são representadas por colchetes "[]" e seus elementos são separados por vírgulas ",". As listas são mutáveis, o que significa que seus elementos podem ser alterados, adicionados ou removidos durante a execução do programa. As listas são muito versáteis e são amplamente utilizadas em programação para armazenar, acessar e manipular dados.
'''

lista.append() #adciona um objeto a lista

lista.clear() #remove todos os elementos da lista

lista.copy()
lista_original = [1, 2, 3, 4]
lista_copia = lista_original.copy()
lista_copia.append(5)
print(lista_original) # saída: [1, 2, 3, 4]
print(lista_copia) # saída: [1, 2, 3, 4, 5]

lista.count()#retorna o elemento na posição
lista = [1, 2, 3, 2, 4, 2]
lista.count(2) #retorna o 3

lista.insert() #(index, objeto) - Insere um elemento em um detrminado index

lista.pop() #remove e retorna o ultimo elemento da lista, caso seja adicionado o Index ele remove e retorna o elemento do index
frutas = ['banana', 'maçã', 'laranja']
laranja = frutas.pop()
print(laranja)  # saída: "laranja"
print(frutas)  # saída: ["banana", "maçã"]
maçã = frutas.pop(1)
print(maçã)  # saída: "maçã"
print(frutas)  # saída: ["banana"]

lista.remove() #remove um elemento
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista) # saida: [1, 2, 4, 5]

#listcomprehension - cria uma lista a partir de uma lista existente ou outra sequência já existente
nova_lista = [expressão for item in sequência if condição]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]

#copias
a = b #funciona como se fosse um ponteiro, então qualquer mudança que ocorrer em a também vai ocorrer em b
a = b[;] #cria uma copia de a em b, as mudanças que acontecerem em a ou b não afetara o outro

#dicionarios
'''
Em Python, um dicionário é uma estrutura de dados que armazena pares de chave-valor, onde cada chave é única e mapeada para um valor correspondente. Os dicionários são estruturas de dados mutáveis, o que significa que os valores associados às chaves podem ser alterados. As chaves dos dicionários devem ser imutáveis, como strings, números ou tuplas, enquanto os valores podem ser de qualquer tipo de objeto. Os dicionários são frequentemente usados em Python para representar estruturas de dados complexas, como configurações, bancos de dados e objetos JSON. Eles podem ser criados usando a sintaxe de chaves {} ou usando o construtor dict().
'''

dicionario.copy() #Copia o dicionario

dicionario.clear() #limpa o dicionario - exclui tudo

dicionario.pop() #(chave) remove e retorna uma chave

dicionario.popitem() # (chave,valor) remove e retorna um item dentro de uma chave

dicionario.update() #Acho que mecla dois dicionarios

#funções
def definição():

def variaveis(a, b):
    return a*b

def encapsulamento (*a): #encapsula a dentro de uma tupla, tem entrada de n variaveis flexiveis

#multiplas saídas
def quadrado_E_cubo(x):
    quadrado = x ** 2
    cubo = x ** 3
    return [quadrado, cubo]

valores = quadrado_E_cubo(3)
print(valores)  # Saída: [9, 27]

#bibliotecas
import math
import random
import time


#Gambiarra para Switch Case
def funcao1():
    print("Função 1")

def funcao2():
    print("Função 2")

def funcao3():
    print("Função 3")

# dicionário com as opções de escolha
opcoes = {
    1: funcao1,
    2: funcao2,
    3: funcao3
}

# exemplo de uso
escolha = 2
opcoes[escolha]()  # chama a função correspondente à escolha
