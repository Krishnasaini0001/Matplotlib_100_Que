import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 20, 25, 30, 35]

lower = [8, 13, 18, 23, 28, 33]
upper = [12, 17, 22, 27, 32, 37]

plt.plot(x, y, label="Mean")
plt.fill_between(x, lower, upper, alpha=0.3, label="Uncertainty")

plt.xlabel("X")
plt.ylabel("Value")
plt.title("Mean with Uncertainty")
plt.legend()

plt.show()