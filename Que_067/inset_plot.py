import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

ax.plot(x, y)
ax.set_title("Main Graph")

inset = ax.inset_axes([0.55, 0.55, 0.35, 0.35])

inset.plot(x, [5, 15, 10, 20, 25])

plt.show()