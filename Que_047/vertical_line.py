import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024, 2025]
sales = [100, 120, 150, 140, 180, 200]

plt.plot(years, sales, marker="o")

plt.axvline(
    2023,
    linestyle="--"
)

plt.title("Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.show()