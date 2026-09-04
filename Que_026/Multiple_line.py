import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_a = [100, 120, 140, 130, 160, 180]
product_b = [80, 110, 100, 150, 140, 170]

plt.plot(months, product_a, linestyle="--", marker="o", label="Product A")
plt.plot(months, product_b, linestyle="-.", marker="s", label="Product B")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.legend()
plt.grid(True)

plt.show()