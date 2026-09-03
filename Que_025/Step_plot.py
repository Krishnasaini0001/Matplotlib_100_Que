import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5, 6]
stock_price = [100, 107, 105, 112, 110, 115]

plt.step(time, stock_price)

plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.title("Stock Price Step Graph")
plt.show()