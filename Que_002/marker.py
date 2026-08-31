import matplotlib.pyplot as plt

# Real data

subjects = [
    "Python",
    "Java",
    "DBMS",
    "OS",
    "DSA"
]

boys_marks = [78, 85, 72, 80, 88]

girls_marks = [82, 79, 85, 76, 60]

# Plot Boys data
plt.plot(subjects, boys_marks, marker="o", linestyle='--', label="Boys")#marker="o" is used to show the data points on the graph
                                                                        #linestyle='--' is used to show the line style as dashed line
# Plot Girls data
plt.plot(subjects, girls_marks, marker="s", label="Girls")#marker="s" is used to show the data points on the graph

# Title
plt.title("Boys vs Girls Average Marks")

# X and Y axis
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

# Legend
plt.legend()

# Show graph
plt.show()