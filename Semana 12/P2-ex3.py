import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(num_pontos):
    x = np.random.uniform(0, 3.14, num_pontos)
    y = np.random.uniform(0, 1, num_pontos)

    pontos_abaixo = np.sum(y <= np.sin(x))

    area_estimada = pontos_abaixo / num_pontos * (np.max(x) - np.min(x))

    return area_estimada

def plot_simulation(num_points, pi_estimate):
    x = np.random.uniform(0, 3.14, num_points)
    y = np.random.uniform(0, 1, num_points)


    points_inside_circle = x * y < 1

    plt.figure(figsize=(5, 5))
    plt.scatter(x[points_inside_circle], y[points_inside_circle], color='blue', label='Inside')
    plt.scatter(x[~points_inside_circle], y[~points_inside_circle], color='red', label='Outside')

    plt.xlim(0, 3.14)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.title(f'Valor da área é: {pi_estimate:.2f}')
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")

    plt.show()


num_points = int(input('Digite o número de pontos: '))

pi_estimate = estimate_pi(num_points)

plot_simulation(num_points, pi_estimate)

##Faltou usar o np.random.uniform
##Faltou finalizar