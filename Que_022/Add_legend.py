import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

plt.plot(x, [10, 20, 30, 40, 50], label="Sales")
plt.plot(x, [5, 15, 25, 35, 45], label="Profit")

plt.xlabel("Months")
plt.ylabel("Amount")
plt.title("Sales and Profit")

plt.legend()
plt.show()