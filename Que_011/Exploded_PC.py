import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
values = [40, 25, 15, 20]

explode = [0.1, 0, 0, 0]

plt.pie(values, labels=labels, explode=explode, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()