import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 35, 25, 50]

plt.plot(x, y, marker="o")

plt.annotate(
    "Highest Value",
    xy=(5, 50),
    xytext=(3.5, 45),
    arrowprops=dict(arrowstyle="->")
)

plt.title("Annotated Graph")
plt.show()