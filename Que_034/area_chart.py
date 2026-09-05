import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
revenue = [100, 130, 90, 190, 130, 270, 310]

plt.plot(years, revenue)
plt.fill_between(years, revenue, alpha=0.3)

plt.xlabel("Year")
plt.ylabel("Revenue")
plt.title("Company Revenue")

plt.show()