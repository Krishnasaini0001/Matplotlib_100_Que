import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]
sales = [100, 150, 120, 180, 200, 170]

plt.bar(months, sales)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()