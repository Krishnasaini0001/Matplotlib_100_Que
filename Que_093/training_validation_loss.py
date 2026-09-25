import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5, 6, 7, 8]

training = [0.9, 0.7, 0.55, 0.43, 0.35, 0.29, 0.25, 0.22]
validation = [0.95, 0.75, 0.60, 0.50, 0.45, 0.43, 0.44, 0.46]

plt.plot(epochs, training, marker="o", label="Training Loss")
plt.plot(epochs, validation, marker="s", label="Validation Loss")

plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.show()