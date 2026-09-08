import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 200]

products = ["Laptop", "Mobile", "Tablet", "Watch"]
product_sales = [50, 90, 40, 30]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Line Graph
ax[0].plot(months, sales, marker="o")
ax[0].set_title("Monthly Sales")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Sales")
ax[0].grid(True)

# Bar Graph
bars = ax[1].bar(products, product_sales)
ax[1].set_title("Product Sales")
ax[1].set_ylabel("Units")

ax[1].bar_label(bars)

plt.tight_layout()
plt.show()