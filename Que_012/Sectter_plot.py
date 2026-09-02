import matplotlib.pyplot as plt

Years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
GDP_growth = [8.26, 6.8, 6.45, 3.87, -6.78, 9.69, 7.61]

plt.scatter(Years, GDP_growth)

plt.xlabel("Years")
plt.ylabel("GDP Growth (in %)")
plt.title("Bharat GDP Growth Over Years")
plt.show()