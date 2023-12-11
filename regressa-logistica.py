import numpy as np
import matplotlib.pyplot as plt

# Função de ativação sigmoide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
 
# Função de normalização
def normalize(data, mean, std):
    return (data - mean) / std
 
# Dados de treinamento
idade_treinamento = np.array([30, 25, 35, 40, 40, 50])
renda_treinamento = np.array([100000, 80000, 120000, 90000, 80000, 110000])
comprou_produto_treinamento = np.array([1, 0, 1, 0, 0, 1])
 
# Normalizando os dados de treinamento
idade_mean = idade_treinamento.mean()
idade_std = idade_treinamento.std()
renda_mean = renda_treinamento.mean()
renda_std = renda_treinamento.std()
 
idade_norm = normalize(idade_treinamento, idade_mean, idade_std)
renda_norm = normalize(renda_treinamento, renda_mean, renda_std)

