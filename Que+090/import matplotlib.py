import matplotlib.pyplot as plt

days = range(1, 11)
price = [100, 103, 101, 106, 110, 108, 115, 118, 116, 122]

plt.plot(days, price, marker="o")

plt.title("Stock Price Movement")
plt.xlabel("Day")
plt.ylabel("Price")

plt.grid(True)
plt.show()