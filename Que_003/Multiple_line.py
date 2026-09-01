import matplotlib.pyplot as plt

subjects = ["OOPs", "DBMS", "DSA", "Python"]

Krishna = [80, 75, 85, 90]
harshendra = [70, 85, 80, 95]
Jatin = [90, 80, 75, 85]
Ajo = [85, 90, 80, 70]
Omprakash = [75, 80, 90, 85]


plt.plot(subjects, Krishna, marker="o", label="Krsna")
plt.plot(subjects, harshendra, marker="s", label="Harv")
plt.plot(subjects, Jatin, marker="^", label="Jatin")
plt.plot(subjects, Ajo, marker="d", label="Ajo")
plt.plot(subjects, Omprakash, marker="v", label="OP")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.legend()
plt.show()