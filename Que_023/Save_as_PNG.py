import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 35, 30]

plt.plot(x, y)

plt.title("Saved Graph")

plt.savefig("my_graph.png", dpi=300, bbox_inches="tight")

plt.show()