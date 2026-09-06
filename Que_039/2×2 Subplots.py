import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

x = [1, 2, 3, 4, 5]

ax[0, 0].plot(x, [1, 4, 9, 16, 25])
ax[0, 0].set_title("Line Plot")

ax[0, 1].bar(x, [5, 10, 15, 20, 25])
ax[0, 1].set_title("Bar Chart")

ax[1, 0].scatter(x, [2, 4, 6, 8, 10])
ax[1, 0].set_title("Scatter Plot")

ax[1, 1].hist([1, 2, 2, 3, 3, 3, 4, 5])
ax[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()