#Methods learned in this file
#1st method is to plot the graph using plt.plot()
#function
#2nd method is to give title to the graph using plt.title()
#3rd method is to give x and y axis using plt.xlabel() and plt.ylabel()
#4th method is to show the legend using plt.legend()

import matplotlib.pyplot as plt

# data
Hit_movies = [
    "RRR",
    "Pushpa 2",
    "Dhurandhar",
    "Tanhaji",
    "Chaava",
    "Kantara 2"
]

years = [2018, 2019, 2020, 2021, 2022, 2023]

Hit_revenue = [724, 867, 567, 625, 404, 664]  # in $M
plt.plot(years, Hit_revenue, marker="o", label="Hit Movies")# Plot Hit movie revenue

# Non-Hit movies
NonHit_movies = [
    "Sui Dhaga",
    "Bajrangi Bhaijaan",
    "Jagga Jasoos",
    "Bhoot Police",
    "Bhediya",
    "Animal"
]

NonHit_revenue = [120, 198, 157, 90, 72, 142]  # in $M
plt.plot(years, NonHit_revenue, marker="o", label="Non-Hit Movies")# Plot Non-Hit movie revenue
plt.title("Hit Movie Revenue VS Non-Hit Movie Revenue")# Title

plt.xlabel("Years")# X and Y axis
plt.ylabel("Revenue (in $M)")

plt.legend()# Show which colour represents which data

plt.show()# Show graph