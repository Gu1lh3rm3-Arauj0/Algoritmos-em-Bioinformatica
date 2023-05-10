#Input
''''
str = input('Input para string')
int = int(input('Input para inteiros'))
float = float(input('Input para reais'))
'''
############################################################
#Print
nome = 'Renata'
idade = 19
altura = 1.71
print('A idade do', nome, 'é', idade, 'e a sua altura é', altura)
print('A idade do {} é {} e a sua altura é {}'.format(nome,idade,altura))
print(f'A idade do {nome} é {idade} e a sua altura é {altura}')
print(f'Bom dia{nome:>20s}');
print(f'Bom dia{2*nome:>20s}');
print(f'Bom dia{nome:_>20s}');
print(f'Bom dia{nome:_<20s}');
print(f'Bom dia{nome:^20s}');
############################################################
#Variaveis Primitivas
a = True
if a:
    print("a é verdadeiro")
else:
    print("a é falso")
#Vai imprimir que a é verdadeiro
############################################################
#STRING 
a= {}
a['nome']= 'renata'
a['sobrenome'] = 'moura'
a['idade'] = 19
a['altura'] =1.71

print (a,"\n")
#saída- {'nome': 'renata', 'sobrenome': 'moura', 'idade': 19, 'altura': 1.71} 
print(a.keys(),"\n")
# saida- dict_keys(['nome', 'sobrenome', 'idade', 'altura']) 
print(a.values(),"\n")
# saida- dict_values(['renata', 'moura', 19, 1.71]) 
print (a.items(),"\n")
#saida- dict_items([('nome', 'renata'), ('sobrenome', 'moura'), ('idade', 19), ('altura', 1.71)]) 

c=a #ta recebendo o lugar da memória
c=a.copy() #recebe as informaçoes
c['nome' ]= 'line'
print(c)
#{'nome': 'line', 'sobrenome': 'moura', 'idade': 19}


    #join() - junta duas strings
palavras = ['renata', 'moura', 'barreto']
frase = ' '.join(palavras)
print(frase)  # saída: 'renata moura barreto'

frase = ', '.join(palavras)
print(frase)  # saída: 'renata, moura, barreto'

    #split() -  divide uma string em uma Lista
frutas = "banana,maçã,uva"
lista_frutas = frutas.split(",")
print(lista_frutas) #["banana", "maçã", "uva"]

    #dividir string - string[inicio:fim]
string = "abcdefghij"
print(string[2:5])   # resultado: "cde"
print(string[:5])    # resultado: "abcde"
print(string[7:])    # resultado: "hij"
print(string[1:8:2])   # resultado: "bdfh"
##################################################################3
#operadores aritmeticos
    # Divisão inteira (//)
    # Resto da divisão ou módulo (%)
    # Potenciação (**)
##################################################################3
#IF, ELSE, ELIF
  # e (and)
  # ou (or)
r = 2
if r == 1:
    print('r não é igual a 1')
elif r== 2:
    print('r é igual a 2')  
else:
    print('r não é igual a 1 ou 2')     
##########################################################################
#comandos de Loop
#for
for i in range(1, 6, 1): #(inicio, fim, passo) ele não vai até o 6
    print(i)
    
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i, end= " ");
    #1 2 3 4 5
    
#ZIP

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

for x, y, z in zip(a, b, c):
    print(x, y, z)
    #vai imprimir:
        #1 a True
        #2 b False
        #3 c True

    #comando enumerate- vai imprimir a posicao
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
    print('aa')
    g += 1

while g >= 5:
    print('bb')
    g -= 1

while g != 5:
    print('cc')
    g += 1

g = 1
while g == 1:
    print('dd')
    g += 1
##################################################################
#Lista
  #COMANDO SET
lista = [1,2,3,4,5,6]
##ll = [3,4,5]
ll= set(lista)
print (lista, "\n") #saida: [1, 2, 3, 4, 5, 6]
print (ll, "\n") #saida: {1, 2, 3, 4, 5, 6} 

z = set([1,2,3,4])
x = set([1,2,3,4,5,6,7,8])
v = z|x

print (v, "\n") #saida: {1, 2, 3, 4, 5, 6, 7, 8}
print(z&x, "\n") #saida:  {1, 2, 3, 4} 
#set meio q mostra oq tem naa lista

poema = 'oi tudo bem?'
letras = set(poema) 
print (letras)#saida: {'?', 'b', 'o', 'i', 'm', 't', ' ', 'd', 'u', 'e'}
freq = {}

for i in letras:
    freq[i] = poema.count(i) #vai mostrar a quantidade de cada coisa
    
print(freq) #{'?': 1, 'b': 1, 'o': 2, 'i': 1, 'm': 1, 't': 1, ' ': 2, 'd': 1, 'u': 1, 'e': 1}

'''
lista.append() #adciona um objeto a lista no final
lista.clear() #remove todos os elementos da lista
lista.copy() #copia
'''
lista_original = [1, 2, 3, 4]
lista_copia = lista_original.copy()
lista_copia.append(5)
print(lista_original) # saída: [1, 2, 3, 4]
print(lista_copia) # saída: [1, 2, 3, 4, 5]

'''''
#lista.count()#retorna o elemento na posição
lista.insert() #(index, objeto) - Insere um elemento em um detrminado index
lista.pop() #remove e retorna o ultimo elemento da lista, caso seja adicionado o Index ele remove e retorna o elemento do index
'''''

lista = [1, 2, 3, 2, 4, 2]
lista.count(2) #retorna o 3


frutas = ['banana', 'maçã', 'laranja']
laranja = frutas.pop()
print(laranja)  # saída: "laranja"
print(frutas)  # saída: ["banana", "maçã"]
a = frutas.pop(1)
print(a)  # saída: "maçã"
print(frutas)  # saída: ["banana"]

#lista.remove() #remove um elemento
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista) # saida: [1, 2, 4, 5]

#listcomprehension - cria uma lista a partir de uma lista existente ou outra sequência já existente
#nova_lista = [expressão for item in sequência if condição]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print(pares) #saida: [2, 4, 6, 8, 10]

#copias
#a = b #funciona como se fosse um ponteiro, então qualquer mudança que ocorrer em a também vai ocorrer em b
##a = b[;] #cria uma copia de a em b, as mudanças que acontecerem em a ou b não afetara o outro

###################################################################################
#DICIONAROS
'''Entre {}, chave: valor
'''
preco= {"celular": 1000, "notebook": 3000}

#imprimir valor do item
valor= preco['celular']
print(valor) #saida= 1000

#adicionar chave
preco["pc"] =13900
print(preco) #{'celular': 1000, 'notebook': 3000, 'pc': 13900}

#ver se existe
if "notebook" in preco:
  print('existe')# vai imprimir

for i in preco:
    print(i) 
    #Vai imprimir: 
        #celular
        #notebook
        #pc

for i in preco.keys():
    print(i) 
    #Vai imprimir: 
        #celular
        #notebook
        #pc

for i in preco.values():
    print(i)
    #Vai imprimir: 
        #1000
        #3000
        #13900

for i, j in preco.items():
    print(i, j)
    #Vai imprimir: 
        #celular 1000
        #notebook 3000
        #pc 13900

#dicionario.copy() #Copia o dicionario
#dicionario.clear() #limpa o dicionario - exclui tudo
#dicionario.pop() #(chave) remove e retorna uma chave
#dicionario.popitem() # (chave,valor) remove e retorna um item dentro de uma chave
#dicionario.update() #Acho que mecla dois dicionarios
#####################################################################################

#FUNÇOES

a=2
b=3
def variaveis(a, b):
    return a*b
  
print (variaveis(a,b)) #saida: 6


#def encapsulamento (*a): #encapsula a dentro de uma tupla, tem entrada de n variaveis flexiveis

#multiplas saídas
def quadrado_E_cubo(a):
    quadrado = a ** 2
    cubo = a ** 3
    return [quadrado, cubo]

valores = quadrado_E_cubo(3)
print(valores)  # Saída: [9, 27]
##############################################################################
#bibliotecas
'''
import math
import random
import time
'''
##################################################################################
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