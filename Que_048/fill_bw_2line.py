import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6]

actual = [100, 120, 140, 130, 160, 180]
predicted = [105, 115, 135, 145, 155, 175]

plt.plot(months, actual, label="Actual")
plt.plot(months, predicted, label="Predicted")

plt.fill_between(
    months,
    actual,
    predicted,
    alpha=0.3
)

plt.xlabel("Month")
plt.ylabel("Value")
plt.title("Actual vs Predicted")
plt.legend()

plt.show()