import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

temperature = [30, 32, 35, 34, 36]
humidity = [60, 65, 70, 68, 72]

fig, ax1 = plt.subplots()

ax1.plot(days, temperature, marker="o")
ax1.set_xlabel("Days")
ax1.set_ylabel("Temperature")

ax2 = ax1.twinx()

ax2.plot(days, humidity, marker="s")
ax2.set_ylabel("Humidity")

plt.title("Temperature and Humidity")

plt.show()