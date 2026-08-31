#method learned from this file;
#1st method is to use marker parameter in marker='o,s' function to show the data points on the graph.
#2nd method is to use linestyle parameter in linestyle='--' function to show the line style as dashed line.
#3rd method is to use color parameter in color='red' function to show the line color as red.

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
plt.plot(subjects, boys_marks, marker="o", linestyle='--',color='red', label="Boys")#marker="o" , linestyle='--', color='red'                                                                   
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