import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 180, 220, 250]
profit = [20, 35, 40, 55, 65]

fig, ax1 = plt.subplots()

ax1.plot(months, sales, marker="o")
ax1.set_xlabel("Months")
ax1.set_ylabel("Sales")

ax2 = ax1.twinx()
ax2.plot(months, profit, marker="s")
ax2.set_ylabel("Profit")

plt.title("Sales vs Profit")
plt.show()