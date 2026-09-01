import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai", "Bhopal", "Pune", "Jaipur"]
population = [20, 21, 2, 7, 4]

plt.barh(cities, population)

plt.xlabel("Population")
plt.ylabel("Cities")
plt.title("City Population")
plt.show()