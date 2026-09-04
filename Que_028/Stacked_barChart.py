import matplotlib.pyplot as plt

departments = ["CSE", "IT", "ECE", "ME"]

male = [60, 50, 45, 70]
female = [40, 50, 55, 30]

plt.bar(departments, male, label="Male")
plt.bar(departments, female, bottom=male, label="Female")

plt.xlabel("Department")
plt.ylabel("Students")
plt.title("Department-wise Students")
plt.legend()

plt.show()