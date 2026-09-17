import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 180, 160, 220, 250]
})

plt.plot(data["Month"], data["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()