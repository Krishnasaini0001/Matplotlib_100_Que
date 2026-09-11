import matplotlib.pyplot as plt

data = [
    [45, 50, 55, 60, 65, 70],
    [55, 60, 65, 70, 75, 80],
    [65, 70, 75, 80, 85, 90]
]

plt.violinplot(data)

plt.xticks(
    [1, 2, 3],
    ["Class A", "Class B", "Class C"]
)

plt.ylabel("Marks")
plt.title("Class Distribution")

plt.show()