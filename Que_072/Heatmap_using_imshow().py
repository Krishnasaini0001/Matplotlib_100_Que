import matplotlib.pyplot as plt
import numpy as np

marks = np.array([
    [80, 75, 90, 85],
    [70, 85, 80, 75],
    [90, 95, 85, 90],
    [65, 70, 75, 80]
])

plt.imshow(marks)

plt.colorbar(label="Marks")

plt.xlabel("Subjects")
plt.ylabel("Students")
plt.title("Student Marks Heatmap")

plt.show()