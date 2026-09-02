import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [1.3, 4.5, 5.7, 6.0, 9.0]
y2 = [10, 9.6, 5.9, 3.88, 1]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Increasing")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Decreasing")

plt.tight_layout()
plt.show()