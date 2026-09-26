import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 160, 220, 250]
profit = [30, 40, 45, 42, 60, 70]

fig, ax1 = plt.subplots()

ax1.plot(months, sales, marker="o")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")

ax2 = ax1.twinx()
ax2.plot(months, profit, marker="s")
ax2.set_ylabel("Profit")

plt.title("Sales vs Profit")
plt.show()