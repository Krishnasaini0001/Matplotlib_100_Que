import matplotlib.pyplot as plt

x = [1, 5, 8, 14, 19]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, marker="o")

plt.text(8, 30, "center")

plt.title("Graph with Annotation")
plt.show()