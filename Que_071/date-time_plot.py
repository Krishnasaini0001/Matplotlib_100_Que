import matplotlib.pyplot as plt
import datetime

dates = [
    datetime.datetime(2026, 1, 1),
    datetime.datetime(2026, 2, 1),
    datetime.datetime(2026, 3, 1),
    datetime.datetime(2026, 4, 1),
    datetime.datetime(2026, 5, 1)
]

sales = [100, 130, 150, 180, 220]

plt.plot(dates, sales, marker="o")

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.gcf().autofmt_xdate()

plt.show()