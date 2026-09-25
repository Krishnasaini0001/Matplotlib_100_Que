import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([
    [85, 10],
    [8, 97]
])

plt.imshow(matrix)

plt.colorbar()

plt.xticks([0, 1], ["Negative", "Positive"])
plt.yticks([0, 1], ["Negative", "Positive"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, matrix[i, j],
                 ha="center",
                 va="center")

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()