import matplotlib.pyplot as plt

fig, ax = plt.subplots(
    2, 2,
    figsize=(10, 7),
    layout="constrained"
)

ax[0, 0].plot([1, 2, 3], [10, 20, 30])
ax[0, 0].set_title("Line")

ax[0, 1].bar(["A", "B", "C"], [20, 30, 15])
ax[0, 1].set_title("Bar")

ax[1, 0].scatter([1, 2, 3], [30, 10, 20])
ax[1, 0].set_title("Scatter")

ax[1, 1].hist([1, 2, 2, 3, 3, 3, 4])
ax[1, 1].set_title("Histogram")

plt.show()