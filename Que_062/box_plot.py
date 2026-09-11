import matplotlib.pyplot as plt

data = [
    [45, 50, 55, 60, 65, 70],
    [55, 60, 65, 70, 75, 80],
    [65, 70, 75, 80, 85, 90]
]

plt.boxplot(
    data,
    tick_labels=["Class A", "Class B", "Class C"]
)

plt.ylabel("Marks")
plt.title("Class-wise Marks")

plt.show()