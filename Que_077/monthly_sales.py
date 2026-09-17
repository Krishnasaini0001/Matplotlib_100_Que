import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 160, 220, 250]

plt.bar(months, sales)

for i, value in enumerate(sales):
    plt.text(i, value + 5, str(value), ha="center")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()