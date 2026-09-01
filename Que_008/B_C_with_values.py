import matplotlib.pyplot as plt

Student = ["Krsna", "Jatin", "Hrv", "Ajo", "Deepak", "Sorda"]
Marks = [90, 50, 40, 30, 60, 75]

bars = plt.bar(Student, Marks)

plt.bar_label(bars)

plt.title("Product Sales")
plt.ylabel("Units Sold")
plt.show()