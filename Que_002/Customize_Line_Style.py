import matplotlib.pyplot as plt

x = ["RRR", "chhaava", "Dhurandar", "KGF", "12th Fail", "Super 30", "MS Dhoni"]
y = [350, 270, 690, 280, 312, 456, 400]

plt.plot(x, y, linestyle="--", marker="o")
plt.title("Performance")
plt.show()