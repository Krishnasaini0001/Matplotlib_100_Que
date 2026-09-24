import matplotlib.pyplot as plt

movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
revenue = [450, 620, 780, 540, 900]

plt.bar(movies, revenue)

max_index = revenue.index(max(revenue))

plt.scatter(
    movies[max_index],
    revenue[max_index],
    s=100
)

plt.annotate(
    "Highest Revenue",
    (movies[max_index], revenue[max_index]),
    xytext=(0, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.title("Movie Revenue Analysis")
plt.ylabel("Revenue ($ Million)")

plt.show()