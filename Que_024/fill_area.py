import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.fill_between(x, y, alpha=0.3)

plt.title("Area Under Curve")
plt.show()