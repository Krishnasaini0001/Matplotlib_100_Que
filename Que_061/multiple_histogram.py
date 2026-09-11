import matplotlib.pyplot as plt

group_a = [45, 50, 55, 60, 65, 70, 75]
group_b = [55, 60, 65, 70, 75, 80, 85]

plt.hist(group_a, bins=5, alpha=0.5, label="Group A")
plt.hist(group_b, bins=5, alpha=0.5, label="Group B")

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.legend()

plt.show()