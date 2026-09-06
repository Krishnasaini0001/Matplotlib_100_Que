import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 20, 35, 40]

plt.plot(x, y, marker="o")

plt.grid(
    axis="y",
    linestyle="--",
    linewidth=0.7
)

plt.title("Performance Graph")

plt.show()