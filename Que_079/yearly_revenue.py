import matplotlib.pyplot as plt

years = [2021, 2022, 2023, 2024, 2025, 2026]
revenue = [450, 520, 610, 700, 820, 950]

plt.plot(years, revenue, marker="o")

plt.title("Yearly Revenue Growth")
plt.xlabel("Year")
plt.ylabel("Revenue ($ Million)")
plt.grid(True)

plt.show()