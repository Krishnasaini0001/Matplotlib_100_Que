import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 160, 220, 250]
profit = [30, 40, 45, 42, 60, 70]

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].plot(months, sales, marker="o")
ax[0].set_title("Monthly Sales")
ax[0].set_ylabel("Sales")

ax[1].bar(months, profit)
ax[1].set_title("Monthly Profit")
ax[1].set_ylabel("Profit")

plt.tight_layout()
plt.show()