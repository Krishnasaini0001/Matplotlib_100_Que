import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
z = [5, 10, 8, 15, 20]

fig = plt.figure()

ax = fig.add_subplot(
    111,
    projection="3d"
)

ax.scatter(x, y, z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title("3D Scatter Plot")

plt.show()