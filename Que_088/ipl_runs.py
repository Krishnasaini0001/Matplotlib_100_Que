import matplotlib.pyplot as plt

teams = ["CSK", "MI", "RCB", "KKR", "SRH"]
runs = [1850, 1420, 1010, 1580, 1350]

plt.bar(teams, runs)

plt.title("Team Total Runs")
plt.xlabel("Team")
plt.ylabel("Runs")

plt.show()