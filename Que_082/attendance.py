import matplotlib.pyplot as plt

students = ["Ajo", "hrv", "krsna", "jatin", "sorabh", "op"]
attendance = [92, 85, 98, 78, 88, 74]

plt.bar(students, attendance)

plt.axhline(75, linestyle="--", label="Minimum Attendance")

plt.title("Student Attendance")
plt.ylabel("Attendance (%)")
plt.legend()

plt.show()