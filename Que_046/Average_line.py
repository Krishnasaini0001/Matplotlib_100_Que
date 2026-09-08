import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 200, 170]

average = sum(sales) / len(sales)

plt.plot(months, sales, marker="o")

plt.axhline(
    average,
    linestyle="--",
    label=f"Average = {average:.1f}"
)

plt.legend()
plt.title("Sales and Average")

plt.show()