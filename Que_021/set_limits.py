import matplotlib.pyplot as plt

x = [1, 4, 6.7, 8.4, 9.5]
y = [10, 96, 35, 80, 90]

plt.plot(x, y)

plt.xlim(1, 9)
plt.ylim(0, 100)

plt.title("Custom Axis Limits")
plt.show()