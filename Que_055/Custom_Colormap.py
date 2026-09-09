import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 15, 30, 25, 40]
values = [10, 20, 30, 40, 50, 60]

plt.scatter(
    x,
    y,
    c=values,
    cmap="viridis",
    s=150
)

plt.colorbar(label="Value")

plt.title("Colored Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()