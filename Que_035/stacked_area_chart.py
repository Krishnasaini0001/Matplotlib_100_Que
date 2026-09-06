import matplotlib.pyplot as plt

years = [2021, 2022, 2023, 2024, 2025, 2026, 2027]

product_a = [20, 30, 40, 50, 60, 70, 80]
product_b = [30, 35, 45, 55, 65, 75, 85]
product_c = [15, 25, 30, 40, 50, 60, 70]

plt.stackplot(
    years,
    product_a,
    product_b,
    product_c,
    labels=["Product A", "Product B", "Product C"]
)

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Product Sales Over Time")
plt.legend()

plt.show()