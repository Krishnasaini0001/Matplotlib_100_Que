import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 80, 200, 170]

min_value = min(sales)
min_index = sales.index(min_value)

plt.bar(months, sales)

plt.text(
    min_index,
    min_value + 5,
    f"Lowest: {min_value}",
    ha="center"
)

plt.title("Sales with Minimum Value")
plt.show()