import matplotlib.pyplot as plt

days = ["Som", "Mangal", "Budh", "Guru", "Shukra", "Shani", "Ravi"]
temperature = [30, 32, 31, 34, 35, 33, 31]

plt.plot(days, temperature, marker="o")

plt.axhline(
    sum(temperature) / len(temperature),
    linestyle="--",
    label="Average"
)

plt.title("Weekly Temperature")
plt.ylabel("Temperature (°C)")
plt.legend()

plt.show()