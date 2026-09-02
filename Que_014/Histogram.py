import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90, 95, 100, 99, 100, 85, 60, 95, 98, 70, 52, 54, 89]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()