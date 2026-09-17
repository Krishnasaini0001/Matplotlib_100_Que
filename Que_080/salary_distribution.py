import matplotlib.pyplot as plt

salary = [
    25000, 28000, 30000, 32000, 35000,
    38000, 40000, 42000, 45000, 50000,
    55000, 60000
]

plt.hist(salary, bins=6, edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()