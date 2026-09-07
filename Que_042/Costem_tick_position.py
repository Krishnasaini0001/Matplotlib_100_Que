import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.xticks(
    [1, 2, 3, 4, 5],
    ["Mon", "Tue", "Wed", "Thu", "Fri"]
)

plt.title("Custom X-axis Labels")

plt.show()