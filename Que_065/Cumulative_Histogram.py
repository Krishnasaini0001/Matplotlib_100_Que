import matplotlib.pyplot as plt

marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(
    marks,
    bins=6,
    cumulative=True
)

plt.xlabel("Marks")
plt.ylabel("Cumulative Frequency")
plt.title("Cumulative Histogram")

plt.show()