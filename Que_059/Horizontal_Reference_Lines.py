import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [85, 45, 72, 30, 90]

plt.bar(students, marks)

plt.axhline(
    40,
    linestyle="--",
    label="Passing Marks"
)

plt.ylabel("Marks")
plt.title("Student Performance")
plt.legend()

plt.show()