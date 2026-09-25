import matplotlib.pyplot as plt

models = ["Logistic Regression", "Decision Tree", "Random Forest", "SVM"]
accuracy = [82, 85, 91, 88]

plt.bar(models, accuracy)

plt.ylabel("Accuracy (%)")
plt.title("Machine Learning Model Accuracy")

plt.xticks(rotation=20)

plt.show()