import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [1200, 1500, 1800, 1600, 2100, 2800, 2500]

plt.plot(days, visitors, marker="o")

plt.fill_between(days, visitors, alpha=0.2)

plt.title("Website Traffic")
plt.xlabel("Day")
plt.ylabel("Visitors")

plt.show()