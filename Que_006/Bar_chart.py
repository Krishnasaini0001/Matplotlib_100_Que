import matplotlib.pyplot as plt

cities = ["Delhi", "Mumbai", "Bhopal", "Pune", "Jaipur"]
population = [20, 21, 2, 7, 4]

plt.bar(cities, population)

plt.xlabel("Cities")
plt.ylabel("Population")
plt.title("City Population")
plt.show()