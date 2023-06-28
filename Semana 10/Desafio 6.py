"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 10 - Desafio 
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    # Gerar coordenadas aleatórias x e y entre 0 e 1
    x = np.random.random(num_points)
    y = np.random.random(num_points)
    
    # Calcular a distância ao quadrado entre cada ponto e a origem (0, 0)
    dist_squared = x**2 + y**2
    
    # Contar quantos pontos estão dentro do círculo unitário (dist_squared < 1)
    num_points_inside = np.sum(dist_squared < 1)
    
    # Estimar a área do círculo (1/4) multiplicada por 4 é igual a π
    pi_estimate = 4 * num_points_inside / num_points
    
    return pi_estimate

def plot_simulation(num_points, pi_estimate):
    # Gerar coordenadas aleatórias x e y entre 0 e 1
    x = np.random.random(num_points)
    y = np.random.random(num_points)
    
    # Calcular a distância ao quadrado entre cada ponto e a origem (0, 0)
    dist_squared = x**2 + y**2
    
    # Verificar quais pontos estão dentro do círculo unitário (dist_squared < 1)
    points_inside = dist_squared < 1
    
    # Plotar os pontos dentro e fora do círculo
    plt.figure(figsize=(5, 5))
    plt.scatter(x[points_inside], y[points_inside], color='blue', label='Inside')
    plt.scatter(x[~points_inside], y[~points_inside], color='red', label='Outside')
    
    # Configurar o aspecto do gráfico
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Mostrar a estimativa de π no título do gráfico
    plt.title(f'Estimate of π: {pi_estimate:.4f}')
    
    # Mostrar a legenda
    plt.legend()
    
    # Exibir o gráfico
    plt.show()

# Solicitar ao usuário o número de pontos a ser utilizado
num_points = int(input('Digite o número de pontos: '))

# Calcular a estimativa de π
pi_estimate = estimate_pi(num_points)

# Plotar o resultado da simulação
plot_simulation(num_points, pi_estimate)
