import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = np.array([120, 150, 180, 160, 220, 250])
profit = np.array([30, 40, 45, 42, 60, 70])
customers = np.array([100, 120, 150, 140, 180, 210])

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Sales Trend
ax[0, 0].plot(months, sales, marker="o")
ax[0, 0].set_title("Sales Trend")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Sales")
ax[0, 0].grid(True)

# 2. Profit
ax[0, 1].bar(months, profit)
ax[0, 1].set_title("Monthly Profit")
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Profit")

# 3. Customers
ax[1, 0].scatter(months, customers, s=100)
ax[1, 0].set_title("Customer Growth")
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Customers")
ax[1, 0].grid(True)

# 4. Sales vs Profit
ax[1, 1].plot(months, sales, marker="o", label="Sales")
ax[1, 1].plot(months, profit, marker="s", label="Profit")
ax[1, 1].set_title("Sales vs Profit")
ax[1, 1].legend()
ax[1, 1].grid(True)

plt.suptitle("Business Data Visualization Dashboard")
plt.tight_layout()

plt.savefig("business_dashboard.png", dpi=300)

plt.show()