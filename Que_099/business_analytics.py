import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch", "Headphone"]

sales = [85, 150, 70, 110, 130]
profit = [20, 35, 15, 25, 30]

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].bar(products, sales)
ax[0].set_title("Product Sales")
ax[0].set_ylabel("Units")

ax[1].bar(products, profit)
ax[1].set_title("Product Profit")
ax[1].set_ylabel("Profit")

for axis in ax:
    axis.tick_params(axis="x", rotation=25)

plt.tight_layout()
plt.show()