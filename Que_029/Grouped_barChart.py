import matplotlib.pyplot as plt
import numpy as np

products = ["Laptop", "Mobile", "Tablet", "Watch"]

sales_2025 = [50, 80, 40, 30]
sales_2026 = [70, 95, 60, 45]

x = np.arange(len(products))
width = 0.35

plt.bar(x - width/2, sales_2025, width, label="2025")
plt.bar(x + width/2, sales_2026, width, label="2026")

plt.xticks(x, products)
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.legend()

plt.show()