import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 200, 170]

max_value = max(sales)
max_index = sales.index(max_value)

plt.bar(months, sales)

plt.text(
    max_index,
    max_value + 5,
    f"Highest: {max_value}",
    ha="center"
)

plt.title("Monthly Sales")
plt.show()