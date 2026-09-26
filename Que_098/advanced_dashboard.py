import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [120, 150, 180, 160, 220, 250]
profit = [30, 40, 45, 42, 60, 70]
customers = [100, 120, 150, 140, 180, 210]
returns = [5, 7, 8, 6, 10, 9]

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].plot(months, sales, marker="o")
ax[0, 0].set_title("Sales")

ax[0, 1].bar(months, profit)
ax[0, 1].set_title("Profit")

ax[1, 0].plot(months, customers, marker="s")
ax[1, 0].set_title("Customers")

ax[1, 1].bar(months, returns)
ax[1, 1].set_title("Returns")

plt.tight_layout()
plt.show()