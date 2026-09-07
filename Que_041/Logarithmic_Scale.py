import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 100, 1000, 10000, 100000]

plt.plot(x, y, marker="o")

plt.yscale("log")

plt.xlabel("X")
plt.ylabel("Value")
plt.title("Logarithmic Scale")

plt.show()