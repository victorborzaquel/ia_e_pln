import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

# plt.plot(x, y)
plt.scatter(x, y, color='red', marker='o')
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de linha")
plt.show()