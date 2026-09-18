import matplotlib.pyplot as plt

students = ["Ajo", "hrv", "krsna", "jatin", "sorabh", "op"]
marks = [78, 85, 92, 67, 88, 74]

plt.bar(students, marks)

plt.axhline(sum(marks) / len(marks), linestyle="--")

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()