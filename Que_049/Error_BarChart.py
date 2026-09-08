import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
values = [10, 15, 13, 20, 18]
errors = [2, 3, 1, 4, 2]

plt.errorbar(
    x,
    values,
    yerr=errors,
    fmt="o"
)

plt.xlabel("Experiment")
plt.ylabel("Measurement")
plt.title("Measurement with Error")

plt.show()