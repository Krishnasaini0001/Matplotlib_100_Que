import matplotlib.pyplot as plt
# data
Hit_movies = [
    "KGF",
    "RRR",
    "pushpa 2",
    "Dhurandar",
    "Dhurandar 2",
    "Taj Story",
    "tanha ji",
    "Chaava",
    "Kantara 2"
]
years = [2018,2019,2020,2021,2022,2023,2024,2025,2026]
Hit_revenue = [724,867,567,625,404,664,779,634,990] #in $M

plt.plot(years,Hit_revenue)

#functions
#1st function  for title
plt.title("Hit movie revenue in each year")
#2nd function for x and y axis 
plt.xlabel("years")
plt.ylabel("Revenue ( in $M )")
plt.show()