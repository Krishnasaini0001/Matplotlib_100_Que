import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_xlabel("Days")
ax.set_ylabel("Sales")

ax_top = ax.secondary_xaxis("top")

ax_top.set_xlabel("Week Number")

plt.show()