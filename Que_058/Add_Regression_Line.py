import matplotlib.pyplot as plt
import numpy as np

hours = np.array([1, 2, 3, 4, 5, 6, 7])
marks = np.array([35, 40, 50, 55, 65, 75, 85])

slope, intercept = np.polyfit(hours, marks, 1)

trend = slope * hours + intercept

plt.scatter(hours, marks, label="Students")
plt.plot(hours, trend, label="Trend Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()

plt.show()