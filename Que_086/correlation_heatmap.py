import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [1.0, 0.8, 0.6],
    [0.8, 1.0, 0.7],
    [0.6, 0.7, 1.0]
])

labels = ["Math", "Science", "English"]

plt.imshow(data)

plt.colorbar()

plt.xticks(range(3), labels)
plt.yticks(range(3), labels)

for i in range(3):
    for j in range(3):
        plt.text(j, i, data[i, j], ha="center", va="center")

plt.title("Subject Correlation Heatmap")
plt.show()