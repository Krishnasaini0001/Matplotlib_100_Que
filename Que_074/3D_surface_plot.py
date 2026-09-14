import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection="3d"
)

ax.plot_surface(X, Y, Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title("3D Surface Plot")

plt.show()