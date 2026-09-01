import matplotlib.pyplot as plt
import numpy as np

Student = ["Krishna", "Jatin", "Hrv", "Ajo", "Deepak", "Sorda"]

persentage_10th = [61, 42, 70, 47, 60, 75]
persentage_12th = [70, 65, 82, 55, 85, 90]
    
x = np.arange(len(Student))
width = 0.35

plt.bar(x - width/2, persentage_10th, width, label="10th")
plt.bar(x + width/2, persentage_12th, width, label="12th")

plt.xticks(x, Student)
plt.ylabel("Percentage %")
plt.title("Yearly Percentage Comparison")
plt.legend()
plt.show()