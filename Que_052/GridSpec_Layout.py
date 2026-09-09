import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

ax1.plot([1, 2, 3, 4], [10, 20, 30, 40])
ax1.set_title("Main Graph")

ax2.bar(["A", "B", "C"], [20, 30, 25])
ax2.set_title("Bar Chart")

ax3.scatter([1, 2, 3], [10, 20, 15])
ax3.set_title("Scatter")

plt.tight_layout()
plt.show()