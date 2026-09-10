import matplotlib.pyplot as plt

income = [20, 35, 50, 65, 80]
population = [10, 20, 15, 30, 25]
size = [100, 300, 500, 700, 1000]

plt.scatter(
    income,
    population,
    s=size,
    alpha=0.5
)

plt.xlabel("Average Income")
plt.ylabel("Population")
plt.title("Bubble Chart")

plt.show()