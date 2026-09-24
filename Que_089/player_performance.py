import matplotlib.pyplot as plt

matches = [10, 15, 20, 25, 30, 35]
runs = [250, 400, 550, 700, 900, 1100]

plt.scatter(matches, runs, s=100)

plt.title("Player Performance")
plt.xlabel("Matches")
plt.ylabel("Runs")

plt.grid(True)
plt.show()