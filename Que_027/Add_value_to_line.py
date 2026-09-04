import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]

plt.plot(months, sales, marker="o")

for i, value in enumerate(sales):
    plt.text(i, value + 5, str(value), ha="center")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()