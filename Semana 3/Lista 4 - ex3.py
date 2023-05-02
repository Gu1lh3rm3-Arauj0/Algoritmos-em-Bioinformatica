"""
Exercicio 3 - Semana 3
A lista de temperaturas de Mons, na Bélgica, foi
armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um
programa que imprima a menor e a maior temperatura,
assim como a temperatura média.
"""
ListaT = [ -10, -8, 0, 1, 2, 5, -2, -4]
ListaT.sort()
print(ListaT[0])
print(ListaT[7])
A = 0

for i in range (0, len(ListaT)):
    A = A + ListaT[i]

print(A/len(ListaT))
