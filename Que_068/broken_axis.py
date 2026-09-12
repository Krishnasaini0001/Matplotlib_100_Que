import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(
    2, 1,
    sharex=True
)

x = [1, 2, 3, 4, 5]
y = [10, 12, 14, 100, 105]

ax1.plot(x, y)
ax2.plot(x, y)

ax1.set_ylim(90, 110)
ax2.set_ylim(0, 20)

ax1.spines["bottom"].set_visible(False)
ax2.spines["top"].set_visible(False)

plt.tight_layout()
plt.show()