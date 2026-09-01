import matplotlib.pyplot as plt

subjects = ["DSA", "Python", "ML", "OOPS"]
hours = [5, 4, 3, 6]

plt.pie(hours, labels=subjects, autopct="%1.1f%%")

plt.title("Study Time Distribution")
plt.show()