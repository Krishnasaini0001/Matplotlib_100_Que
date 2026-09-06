import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
values = [40, 25, 15, 20]

plt.pie(values, labels=labels, autopct="%1.1f%%")

circle = plt.Circle((0, 0), 0.6, color="white")
plt.gca().add_artist(circle)

plt.title("Programming Language Usage")

plt.show()