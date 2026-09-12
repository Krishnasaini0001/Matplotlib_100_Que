import matplotlib.pyplot as plt
import numpy as np

angles = np.linspace(0, 2 * np.pi, 8)
values = [2, 4, 6, 5, 7, 4, 3, 5]

fig, ax = plt.subplots(
    subplot_kw={"projection": "polar"}
)

ax.plot(angles, values)

ax.set_title("Polar Plot")

plt.show()