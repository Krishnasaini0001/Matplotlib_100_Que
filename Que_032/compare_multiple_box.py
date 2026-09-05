import matplotlib.pyplot as plt

math = [55, 60, 65, 70, 75, 80, 85]
science = [50, 58, 62, 68, 72, 78, 82]
english = [60, 65, 70, 75, 80, 85, 90]

data = [math, science, english]

plt.boxplot(data, label=["Math", "Science", "English"])

plt.ylabel("Marks")
plt.title("Subject-wise Marks Distribution")

plt.show()