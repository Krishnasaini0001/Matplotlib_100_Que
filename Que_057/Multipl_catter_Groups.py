import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4]
y1 = [10, 20, 15, 25]

x2 = [1, 2, 3, 4]
y2 = [20, 15, 30, 35]

plt.scatter(x1, y1, label="Group A")
plt.scatter(x2, y2, label="Group B")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Group Comparison")
plt.legend()

plt.show()