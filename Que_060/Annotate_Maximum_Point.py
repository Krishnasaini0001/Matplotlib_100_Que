import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 130, 180, 150, 220, 190]

max_index = sales.index(max(sales))

plt.plot(months, sales, marker="o")

plt.annotate(
    "Maximum Sales",
    xy=(max_index, sales[max_index]),
    xytext=(max_index - 1, sales[max_index] - 30),
    arrowprops=dict(arrowstyle="->")
)

plt.title("Maximum Sales Point")
plt.show()