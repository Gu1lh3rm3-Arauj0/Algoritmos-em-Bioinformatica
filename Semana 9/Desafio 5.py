"""
Guilherme AraÃºjo Mendes de Souza
UNIFESP - ICT
alg bio

Lista 9 - Desafio
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import convolve
"""
imagem = plt.imread('torax.jpg')

imagem_array = np.array(imagem)

imagem_array = imagem / 255.0

imagem_array = 1 - imagem

limite = 0.5
imagem_array = np.where(imagem < limite, 0, 1)

filtro = np.ones((3, 3)) / 9
imagem_array = convolve2d(imagem, filtro, mode='same', boundary='symm')


plt.imshow(imagem_array, cmap='gray')
plt.axis('off')
plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Carregar a imagem biomédica em escala de cinza
imagem = plt.imread("torax.jpg")

# Definir o limite do threshold
limite = 0.5

# Definir o filtro de média 3x3
filtro = np.ones((3, 3)) / 9

# Aplicar a transformação de negativo
imagem_negativa = 1 - imagem

# Aplicar o thresholding
imagem_thresholded = np.where(imagem < limite, 0, 1)

# Aplicar o filtro de média
imagem_filtrada = convolve(imagem, filtro, mode='reflect')

# Configurar a exibição das imagens em uma única figura
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Exibir a imagem original
axs[0, 0].imshow(imagem, cmap='gray')
axs[0, 0].set_title("Imagem Original")
axs[0, 0].axis('off')

# Exibir a imagem com o negativo
axs[0, 1].imshow(imagem_negativa, cmap='gray')
axs[0, 1].set_title("Imagem com Negativo")
axs[0, 1].axis('off')

# Exibir a imagem binarizada após o thresholding
axs[1, 0].imshow(imagem_thresholded, cmap='gray')
axs[1, 0].set_title("Imagem Binarizada")
axs[1, 0].axis('off')

# Exibir a imagem após o filtro de média
axs[1, 1].imshow(imagem_filtrada, cmap='gray')
axs[1, 1].set_title("Imagem Filtrada")
axs[1, 1].axis('off')

# Ajustar o espaçamento entre as imagens
plt.tight_layout()

# Exibir a figura com as imagens
plt.show()