import matplotlib.pyplot as plt

marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 80, 85, 90]

plt.violinplot(marks)

plt.ylabel("Marks")
plt.title("Marks Distribution")

plt.show()