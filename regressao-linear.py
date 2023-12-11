import matplotlib.pyplot as plt

X = [1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2] # Altura
y = [60,62,64,66,68,70,72,74] # Peso

n = len(X)
sx = sum(X)
sy = sum(y)
sxy = sum([X[i] * y[i] for i in range(n)])
sx2 = sum([X[i] ** 2 for i in range(n)])

m = (n * sxy - sx * sy) / (n * sx2 - (sx ** 2))
b = (sy / n) - m * (sx / n)

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