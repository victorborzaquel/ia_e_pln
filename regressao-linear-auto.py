import matplotlib.pyplot as plt
import numpy as np

X = np.array([1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2]) # Altura
y = np.array([60,62,64,66,68,70,72,74]) # Peso

m, b = np.polyfit(X, y,1)

def predict_peso(altura):
  return m * altura + b

altura_prev = 1.75
peso_prev = predict_peso(altura_prev)

plt.plot(altura_prev, peso_prev, marker="o", markeredgecolor="red", markerfacecolor="green")
plt.scatter(X,y)

x0, x1 = plt.xlim()
y0, y1 = plt.ylim()

plt.axline(xy1=(0,b), slope=m, linestyle="--", color="k")
plt.xlim(x0,x1)
plt.ylim(y0,y1)

plt.show()