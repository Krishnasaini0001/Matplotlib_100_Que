import matplotlib.pyplot as plt
import numpy as np

categories = [
    "Python",
    "Java",
    "SQL",
    "ML",
    "DSA"
]

values = [8, 7, 9, 6, 8]

angles = np.linspace(
    0,
    2 * np.pi,
    len(categories),
    endpoint=False
)

values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig, ax = plt.subplots(
    subplot_kw={"projection": "polar"}
)

ax.plot(angles, values)
ax.fill(angles, values, alpha=0.2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

ax.set_title("Skill Radar Chart")

plt.show()