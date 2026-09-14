import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales = [100, 150, 130, 180, 220]
profit = [20, 30, 25, 45, 60]

products = ["Laptop", "Mobile", "Tablet", "Watch"]
product_sales = [50, 90, 40, 30]

fig, ax = plt.subplots(
    2, 2,
    figsize=(12, 8)
)

# 1. Sales Trend
ax[0, 0].plot(
    months,
    sales,
    marker="o"
)
ax[0, 0].set_title("Sales Trend")

# 2. Profit Trend
ax[0, 1].plot(
    months,
    profit,
    marker="s"
)
ax[0, 1].set_title("Profit Trend")

# 3. Product Sales
bars = ax[1, 0].bar(
    products,
    product_sales
)
ax[1, 0].bar_label(bars)
ax[1, 0].set_title("Product Sales")

# 4. Sales Distribution
ax[1, 1].pie(
    product_sales,
    labels=products,
    autopct="%1.1f%%"
)
ax[1, 1].set_title("Sales Distribution")

fig.suptitle(
    "Company Sales Dashboard",
    fontsize=16
)

plt.tight_layout()
plt.show()