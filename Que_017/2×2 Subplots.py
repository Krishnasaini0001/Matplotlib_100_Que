import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

plt.subplot(2, 2, 1)
plt.plot(x, [1, 4, 9, 16, 25])
plt.title("Line")

plt.subplot(2, 2, 2)
plt.bar(x, [5, 10, 15, 20, 25])
plt.title("Bar")

plt.subplot(2, 2, 3)
plt.scatter(x, [2, 4, 6, 8, 10])
plt.title("Scatter")

plt.subplot(2, 2, 4)
plt.hist([1, 2, 2, 3, 3, 3, 4, 5])
plt.title("Histogram")

plt.tight_layout()
plt.show()