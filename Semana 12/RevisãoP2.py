"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Revisão - P2
Esse codigo tem intuito de servir de revisão para a prova de Algoritmos em BioInformática
portanto o mesmo não tem funcionalidade
"""

###Leitura de arquivos

##Criando um objeto

#Criando um arquivo Objeto
teste = open('Arquivo.txt', 'r') #Cria ou abre um arquivo - open( nome_arq,acess_mode)

#Modos de acesso
"""
‘r’: modo de leitura
‘r+’: modo de leitura e escrita
‘w’: modo de escrita
‘w+’: modo de leitura e escrita
‘a’: modo de apend
a+’: modo de append e leitura
"""

##MÉTODOS DO OBJETO

#Leitura do arquivo
n = 1 #Exemplo
teste.read(n) #lê n bytes em forma de string
teste.readlines(n) #lé n linhas do arquivo. Se n não for declarado, le
teste.readlines() #le todas as linhas do arquivo e organiza em uma lista

#Escrita no arquivo
lista = [] # exemplo
teste.write(str)#escreve a string (str) no arquivo
teste.writelines(lista)#escreve todas as strings contidas na lista


###Numpy
"""
O NumPy é uma biblioteca para a linguagem de programação
Python que adiciona suporte para cálculo matricial de forma
eficiente. Possui suporte para matrizes multidimensionais,
além de com uma grande coleção de funções matemáticas de
alto nível para operar nessas matrizes.
"""

##Criando um NDARRAY
import numpy as np
m = [[1,2,3],[4,5,6],[7,8,9]]
mdarray = np.array(m)

m[0,0] #Pega o elemento 00 da matriz, portanto ele pegara o elemento 1
m[1,0] #Vai pegar o 4
m[1,-1] #Pega o ultimo elemento da linha 1 (6)
m[0:2,0] #Pega os primeiros elementos da linha 0 e 1 ([1][4])
m[0:2,1:3] #Pega os elementos da linha 0 e 1 e coluna 1 e 2 ([2,3][5,6])

##EXTRAINDO INFORMAÇÕES DO NDARRAY
m.ndim #Retorna o numero de dimensões (2)
m.shape #Retorna o formado da matriz (3,3)
m.size #Retorna a quantidade de elementos (9)
m.dtype #Retorna o tipo de elemento (int32)


m = np.array([[1,2,3,4,5,6]]) #criar um array a partir de uma conjunto de listas np.array([[Listas]])

m = np.arange(1,10,1) #criar um array similar ao comando range - np.arange(P_inicial,P_final,Passo)

np.zeros((2,2)) #criar um array contendo elementos zeros - np.zeros((formato))

np.ones((2,2)) #criar um array contendo elementos uns - np.ones((formato))

np.zeros_like(m) #criar um array contendo elementos zeros mesmo formato da input - np.zeros_like(array)

m = np.linspace(0,1,5) #criar um array contendo elementos igualmente espaçados entre p_inicial e p_final de t=tamanho - np.linspace(p_inicial,p_final,tamanho)

m = np.random.randint(1,100,(1,1)) #Criar um array contendo números aleatórios inteiros entre min e max no formato - np.random.randint(min,max,(formato))

##Tipos de Variáveis 
"""
np.bit Um bit pode assumir somente 2 valores: 0 ou 1
np.int8 Inteiro (-128 até 127)
np.int16 Inteiro (-32768 até 32767)
np.int32 Inteiro (-2147483648 até 2147483647)
np.int64 Inteiro (-9223372036854775808 até 9223372036854775807)
np.uint8 Inteiro absoluto (0 até 255)
np.uint16 Inteiro absoluto (0 até65535)
np.uint32 Inteiro absoluto (0 até 4294967295)
np.uint64 Inteiro absoluto (0 até 18446744073709551615)
Np.bool Variável boleana
np.float32 Ponto flutuante com 32 bits
np.float64 / np.float_ Ponto flutuante com 64 bits
np.complex64 Número complexo representado por 2 numeros flutuantes de 32 bits
np.complex128 Número complexo
"""
m = m.astype('int64') #METODO .ASTYPE - Com o método astype pode-se alterar o tipo de variável do array.


##Operações com matrizes
"""
Lembrando, os operadores em Python são:
+ Adição
- Subtração
* Multiplicação
/ Divisão
** Potenciação
// Divisão Inteira
% Resto da Divisão
"""

#Soma
a = np.array([[4,6,7],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a+b

#subtração
a = np.array([[4,6,7],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a-b

#Multiplicação
a = np.array([[4,6,7],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a*b
#Obs: Multiplica elemento A11 por Elemento B11

#Divisão
a = np.array([[4,6,7],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a/b
#OBS: Divide elemento A11 por elemento B11

#Divisão Inteira
a = np.array([[4,6,7],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a//b
#OBS: Divide elemento A11 por elemento B11 e retorna um numero inteiro

# Potenciação
a = np.array([[4,6,7],[8,2,3]])
b = np.array([[5,9,10],[9,13,11]])
c = a**b
#OBS: Eleva o elemento A11 por B11

#Subtração por um escalar
b = np.array([[5,9,10],[9,13,11]])
c = 3-b

#Divisão por um escalar
b = np.array([[5,9,10],[9,13,11]])
c = b/3

#multiplicação por um escalar
b = np.array([[5,9,10],[9,13,11]])
c = b*3


##Operações Matriciais
#MULTIPLICAÇÃO DE MATRIZ- NP.DOT(A,B)
a = np.array([[4,6],[8,2]])
b = np.array([[5,3],[9,4]])
c = np.dot(a,b)

#MATRIZ INVERSA - NP.LINALG.INV(A)
a = np.array([[4,6],[8,2]])
b = np.linalg.inv(a)

#DETERMINANTE - NP.LINALG.DET(A)
a = np.array([[4,6],[8,2]])
b = np.linalg.det(a)

#MATRIZ TRANSPOSTA - .T
a = np.array([[4,6,2],[8,2,4]])
b = a.transpose()
B = a.T


##Extraindo informações da Matriz
#MINIMO MATRIZ - .MIN()
a = np.array([[2,5,3],[8,6,9]])
print(a.min()) # valor maximo da matriz
print(a.min(0)) # valor maximo dos elementos ao longo do eixo 1
print(a.min(1)) # valor maximo dos elementos ao longo do eixo 0

#MAXIMO MATRIZ - .MAX()
a = np.array([[2,5,3],[8,6,9]])
print(a.max()) # valor maximo da matriz
print(a.max(0)) # valor maximo dos elementos ao longo do eixo 1
print(a.max(1)) # valor maximo dos elementos ao longo do eixo 0

#SOMA MATRIZ - .SUM()
print(a.sum()) # media todos os elementos da matriz
print(a.sum(0)) # media os elementos ao longo do eixo 1
print(a.sum(1)) # media os elementos ao longo do eixo 0

#SOMA COMULATIVA MATRIZ - .CUMSUM()
a = np.array([[2,5,3],[8,6,9]])
print(a.cumsum()) # soma acumulativa

#MEDIA MATRIZ - .MEAN()
a = np.array([[2,5,3],[8,6,9]])
print(a.mean()) # media de todos os elementos
print(a.mean(0)) # media os elementos ao longo do eixo 1
print(a.mean(1)) # media os elementos ao longo do eixo 0

#DESVIO PADRÃO MATRIZ - .STD()
a = np.array([[2,5,3],[8,6,9]])
print(a.std()) # desvio padrão de todos os elementos
print(a.std(0)) # desvio pad os elementos ao longo do eixo 1
print(a.std(1)) # desvio pad os elementos ao longo do eixo 0


##FUNÇÕES MATEMÁTICAS
angle = np.linspace(0,2*np.pi,3)
sinvalue = np.sin(angle)
print(angle)
print(sinvalue)

"""
np.sin(x) Seno
np.cos(x) Cosseno
np.tan(x) Tangente
np.arcsin(x) Arcseno
np.arccos(x) Arccosseno
np.arctan(x) Arctangente
np.hypot(a,b) Hipotenusa
np.deg2rad(x) Converte angulos de radianos para graus
np.rad2deg(x) Converte angulos de graus para radianos
np.deg2rad(x) Converte angulos de graus para radianos
np.rad2deg(x) Converte angulos de radianos para graus
np.absolute(x) Retorna o valor absoluto
np.exp2(x) Retorna valor 2^x
np.log(x) Retorna o log de e. e-> numero de euler
np.log10(x) Retorna o log na base 10
np.log2(x) Retorna o log na base 2
np.angle() Retorna o ângulo da parte complexa
np.real() Retorna a parte real de um numero complex
np.imag() Retorna a parte imaginaria de um número complexo
np.conj(x) Retorna o valor conjulgado
Np.sqrt(x) Retorna a raiz quadrada
np.cbrt(x) Retorna a raiz cubica
np.around(x) Faz o arredondamento
np.floor(x) retorna o número inteiro inferior
np.ceil(x) retorna o número inteiro superior
np.trunc(x) Retorna o valor inteiro truncado
"""

##REFORMATANDO ARRAYS
mat = np.ones((4,3))
print(mat.shape)
mat2col = mat.reshape(6,2)
print(mat2col.shape)
mat1col = mat.reshape(12,1)
print(mat1col.shape)

#USANDO RESHAPE(-1)
mat = np.ones((4,3))
print(mat.shape)
mat2col = mat.reshape(-1,2)


print(mat2col.shape)
mat1col = mat.reshape(-1,1)
print(mat1col.shape)
mat0col = mat.reshape(-1)
print(mat0col.shape)

#COCATENAÇÃO VERTICAL
a = np.ones((4,4))
b =3*np.ones((3,4))
c = np.vstack((a,b))
print(c)
print(40*'-')
d =np.concatenate((a,b,5*a)==0)
print(d)
#OBS: Todas as matrizes precisam ter o mesmo numero de colunas

#COCATENAÇÃO HORIZONTAL
a = np.ones((4,5))
b = 3*np.ones((4,3))
c = np.hstack((a,b))
print(c)
print(40*'-')
d = np.concatenate((a,b),axis=1)
print(d)
#OBS: Todas as matrizes precisam Eixo 1ter o mesmo numero de linhas

#CRIANDO REPETIÇOES
a = np.random.randint(0,4,(3,3))
b = np.tile(a,(2,1))
c = np.tile(a,(1,2))
d = np.tile(a,(2,2))

##ARRAYS BOLEANOS

#All False
allfalse = np.zeros((2,2),dtype='bool')
print(allfalse)

#All True
alltrue = np.ones((2,2)).astype('bool')
print(alltrue)

#Exemplo
a = np.random.randint(0,10,(3,3))
sel = a > 5
print(a)
print(sel)

#FATIAMENTO DE ARRAYS
m = np.arange(1,10).reshape(3,3)
a = m[:2,1:]
b = m[-1,:]

#FATIAMENTO COM BOLEANOS
a = np.arange(0,6)
sel = a>=3
b = a[sel]

#SUBSTITUINDO VALORES COM BOLEANOS
a = np.array([[0,5,1],[1,5,6],[7,7,5]])
sel = a > 5
a[sel] = -5
print(a)

#outro exemplo
a = np.array([[0,5,1],[1,5,6],[7,7,5]])
b = -5*np.ones((3,3))
sel = a>5

a = np.array([[0,5,1],[1,5,6],[7,7,5]])
b = -5*np.ones((3,3))
sel = a>5
b[sel] = a[sel]

#OBS: Só posso fazer este tipo de substituição se as matrizes A e B tiver o mesmo Foramato (Shape)

##COMANDO OR AND AND NOT EM NUMPY
a = np.array([5])
sel = (a>1) & (a < 4)
sel2 = (a > 2) | (a >= 22)
sel3 = ~ a != 4

##FUNÇÕES NUMPY

NP.SAVEZ(FILE,*VAR)
#OBS: Os arquivos salvos em numpy tem extenção .npz

NP.LOAD(FILE,*VAR)

NP.LOADTXT (ARQ)

NP.SAVETXT (ARQ)

###Matplotlib
import matplotlib.pyplot as plt

PLT.CLOSE(‘ALL’) #Este comando fecha todas as janelas contendo gráficos no spyder

PLT.READIMAGE(ARQ)

PLT.SAVEFIG(NAME)

#Matplotlib possui um conjunto de submódulos
matplotlib.pyplot #é uma interface baseada nos comandos de Matlab

matplotlib.image #uma interface para imagens

Matplotlib.mlab #Funções python numéricas escritas para compatibilidade com comandos MATLAB com os mesmos nomes. Muito Util para processamento de sinais

#PLOT - Grafico de linhas
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.scatter(x,y)
plt.show()

#BAR - Grafico de barras
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.bar(x,y)
plt.show()

#BARH - Grafico de barras na horizontal
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.barh(x,y)
plt.show()

#PIE - Grafico de pizza
x = np.arange(0,20)
y = np.random.randint(0,10,(20))
plt.pie(x)
plt.show()

##CUSTOMIZANDO O GRAFICO
x = np.arange(-20,21)
y = x**2 -1
plt.plot(x,y)
plt.show()

#Adicionando um titulo
x = np.arange(-20,21)
y = x**2 -1
plt.plot(x,y)
plt.title('meu grafico')
plt.show()

#Adicionando Eixo X
x = np.arange(-20,21)
y = x**2 -1
plt.plot(x,y)
plt.title('meu grafico’)
plt.xlabel(‘eixo x’)
plt.show()

#Adicionando Eixo Y
x = np.arange(-20,21)
y = x**2 -1
plt.plot(x,y)
plt.title('meu grafico’)
plt.xlabel(‘eixo x’)
plt.ylabel(‘eixo y’)
plt.show()

#Adicionando grades
x = np.arange(-20,21)
y = x**2 -1
plt.plot(x,y)
plt.title('meu grafico’)
plt.xlabel(‘eixo x’)
plt.ylabel(‘eixo y’)
plt.grid()
plt.show()

##MULTIPLOS GRÁFICOS
x = np.arange(-20,21)
y = x**2 -1
yy = x + 2
plt.plot(x,y,'ro', linewidth=2)
plt.plot(x,yy,'go--', linewidth = 5)
plt.title('meu grafico')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.grid()
plt.xlim((-10,10))
plt.ylim((-50,100))
plt.show()

#MULTIPLOS GRÁFICOS - FOR
x = np.linspace(-1,1,100)
for i in range(1,5):
plt.plot(x,x**i)
plt.show()

#MULTIPLOS GRÁFICOS - SUBPLOTS
Plt.subplot(2,2,x)

x = np.arange(-20,21)
plt.subplot(2,2,1)
plt.plot(x,x)
plt.subplot(2,2,2)
plt.bar(x,x**2)
plt.subplot(2,2,4)
plt.scatter(x,x**3,linewidth = 3)
plt.show()

x = np.linspace(-1,1,100)
for i in range(1,7):
plt.subplot(2,3,i)
plt.plot(x,x**i)
plt.title(f'polinomio de {i} ord ')
plt.show()