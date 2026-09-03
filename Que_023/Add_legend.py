import matplotlib.pyplot as plt

hit_movies = ["RRR", "chhaava", "Dhurandar", "KGF", "12th Fail", "Super 30", "MS Dhoni"]
revenue = [350, 270, 690, 280, 312, 456, 400]

plt.plot(hit_movies, revenue)
plt.xlabel("Hit Movies")
plt.ylabel("Revenue (in $M)")
plt.title("Movie Revenue Over the Years")

plt.legend()
plt.show()