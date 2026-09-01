import matplotlib.pyplot as plt

movies = ["RRR", "chhaava", "Dhurandar", "KGF", "12th Fail", "Super 30", "MS Dhoni"]
revenue = [350, 270, 690, 280, 312, 456, 400]

plt.plot(movies, revenue, marker="o",color="black", linestyle="--", linewidth=2, markersize=8    )
plt.grid(True)

plt.title("Movie Revenue Over the Years")
plt.xlabel("Movies")
plt.ylabel("Revenue (in $M)")
plt.show()