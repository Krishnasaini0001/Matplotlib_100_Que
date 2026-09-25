import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5, 6, 7, 8]
loss = [0.90, 0.70, 0.55, 0.43, 0.35, 0.29, 0.25, 0.22]

plt.plot(epochs, loss, marker="o")

plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.grid(True)
plt.show()