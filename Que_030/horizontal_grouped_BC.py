import matplotlib.pyplot as plt
import numpy as np

languages = ["Python", "Java", "C++", "JavaScript"]

students_2025 = [80, 60, 40, 70]
students_2026 = [95, 65, 50, 85]

y = np.arange(len(languages))
width = 0.35

plt.barh(y - width/2, students_2025, width, label="2025")
plt.barh(y + width/2, students_2026, width, label="2026")

plt.yticks(y, languages)
plt.xlabel("Students")
plt.title("Programming Language Preference")
plt.legend()

plt.show()