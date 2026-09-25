import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
low = [95, 98, 100, 102, 105]
high = [105, 108, 110, 112, 115]

plt.plot(days, low, label="Low")
plt.plot(days, high, label="High")

plt.fill_between(days, low, high, alpha=0.2)

plt.title("Stock High-Low Range")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()

plt.show()